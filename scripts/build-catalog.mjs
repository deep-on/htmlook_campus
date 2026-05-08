#!/usr/bin/env node
/**
 * htmlook_campus catalog builder.
 *
 * - profiles/<id>/profile.json → entry { type: "profile", ... }
 * - sample_workspaces/<id>/ → entry { type: "workspace_seed", ... }
 *   (uses_profiles 는 sample 안의 .htmlook/workspace.json 에서 추출, 없으면 ["hyperframes"] 기본)
 *
 * 사용:
 *   node scripts/build-catalog.mjs > catalog.json
 *
 * CI:
 *   .github/workflows/catalog.yml 이 매 push 마다 호출.
 */

import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const PROFILES_DIR = path.join(ROOT, 'profiles');
const SAMPLES_DIR = path.join(ROOT, 'sample_workspaces');
const TODAY = new Date().toISOString().slice(0, 10);

function dirSizeKb(dir) {
  let total = 0;
  const stack = [dir];
  while (stack.length) {
    const cur = stack.pop();
    for (const entry of fs.readdirSync(cur, { withFileTypes: true })) {
      const p = path.join(cur, entry.name);
      if (entry.isDirectory()) stack.push(p);
      else if (entry.isFile()) total += fs.statSync(p).size;
    }
  }
  return Math.round(total / 1024);
}

function collectProfiles() {
  if (!fs.existsSync(PROFILES_DIR)) return [];
  const out = [];
  for (const id of fs.readdirSync(PROFILES_DIR).sort()) {
    const dir = path.join(PROFILES_DIR, id);
    if (!fs.statSync(dir).isDirectory()) continue;
    const manifestPath = path.join(dir, 'profile.json');
    if (!fs.existsSync(manifestPath)) continue;
    const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
    out.push({
      type: 'profile',
      id: manifest.id,
      name: manifest.name,
      category: manifest.category ?? 'misc',
      description: manifest.description ?? '',
      tags: manifest.tags ?? [],
      size_kb: dirSizeKb(dir),
      path: `profiles/${id}/`,
      license: manifest.license ?? 'MIT',
    });
  }
  return out;
}

function collectSeeds() {
  if (!fs.existsSync(SAMPLES_DIR)) return [];
  const out = [];
  for (const id of fs.readdirSync(SAMPLES_DIR).sort()) {
    const dir = path.join(SAMPLES_DIR, id);
    if (!fs.statSync(dir).isDirectory()) continue;
    let usesProfiles = ['hyperframes'];
    let description = `${id} sample workspace`;
    let category = 'sample';
    const wsJsonPath = path.join(dir, '.htmlook', 'workspace.json');
    if (fs.existsSync(wsJsonPath)) {
      try {
        const ws = JSON.parse(fs.readFileSync(wsJsonPath, 'utf8'));
        if (ws.profiles) {
          usesProfiles = Object.keys(ws.profiles).filter(p => ws.profiles[p].active);
        }
        if (ws.description) description = ws.description;
        if (ws.category) category = ws.category;
      } catch {
        // ignore parse errors — fall back to defaults
      }
    }
    out.push({
      type: 'workspace_seed',
      id,
      name: id.replace(/[-_]/g, ' '),
      category,
      uses_profiles: usesProfiles,
      description,
      tags: [id, ...usesProfiles],
      size_kb: dirSizeKb(dir),
      path: `sample_workspaces/${id}/`,
      license: 'CC0',
    });
  }
  return out;
}

const catalog = {
  version: 1,
  schema: 'htmlook-catalog/v1',
  updated_at: TODAY,
  entries: [...collectProfiles(), ...collectSeeds()],
};

process.stdout.write(JSON.stringify(catalog, null, 2) + '\n');
