# Step 6 · Save-as-Skill (catturare un workflow)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <b>Italiano</b>
</p>

> Il ciclo cite + apply_edit imparato nello Step 5 — *l'app se lo
> ricorda*. La prossima volta, un clic lo riesegue.
> ~ 5 min.

Alla fine di questo step avrai uno strumento tuo registrato nel
workspace e visibile nella sezione *Tools* della sidebar (o nel quick
launcher ⌘K · Add wizard).

## 6.1 · *Save as Skill* — ingresso

Se l'ultimo giro con l'LLM / ciclo apply_edit è andato bene, clic sul
*⋯* in alto del pannello AI a destra → **Save as Skill**.

Il dialog chiede tre righe:

| Campo | Esempio |
|---|---|
| Name | *Tighten subtitle* |
| When to use | *quando un sottotitolo è troppo corto, espanderlo a una riga* |
| Default prompt | *Espandi il sottotitolo nella regione cite corrente con il valore di Apex (edge compute, deploy veloce) e apply_edit* |

> Video: [ADV · Add a tool. Three fields.](../videos/features/12-advanced-06-tool-wizard.mp4) (30 s)

## 6.2 · Dove vive

`.htmlook/skills/<name>.skill.json` (dentro al workspace, spec v0.3).
Condividi il workspace e i colleghi hanno lo skill anche loro.

Per usarlo ovunque — **Settings → Skills → Promote to global**.

## 6.3 · Chiamarlo dall'Add wizard

⌘K o il *+* nella sidebar → il catalogo più i tuoi skill compaiono
come card. Clic su una card → esegue da solo con il contesto di
selezione corrente.

## 6.4 · Spec Skill v0.3 — cosa c'è dentro

```json
{
  "name": "tighten-subtitle",
  "version": "0.3",
  "description": "...",
  "default_prompt": "...",
  "needs": ["selection_html", "active_file"],
  "produces": ["apply_edit"]
}
```

`needs` / `produces` sono nomi di strumenti MCP. Spec completa nel
repo principale di HTMLook in `docs/skills/v0.3.md` (pubblico al v1.0
GA).

## 6.5 · Skill vs Profile

- **Skill** = cattura di un'*azione* (un prompt + combinazione di
  strumenti). Locale al workspace o user-global.
- **Profile** = bundle di *strumenti + contenuto seed + Skill*. La
  v1.0 ne porta 8 ([Step 7](../07-bundled-profiles/)).

Come scrivere il tuo Profile sta in [Step 8 · extend](../08-extend/).

## ✅ Checkpoint Step 6

- Hai aperto il dialog *Save as Skill* nel pannello AI a destra.
- Hai riempito le tre righe e salvato uno skill.
- Lo skill compare come card nel ⌘K — clic lo riesegue.

Tutti e tre? → [Step 7 · bundled profiles](../07-bundled-profiles/)

## Per approfondire

- [`../05-command/personas/`](../05-command/personas/) — immagina
  ogni persona salvata come skill. Il pattern si vede subito.
