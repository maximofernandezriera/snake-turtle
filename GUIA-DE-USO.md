# Guía de uso — cómo lanzar el Snake

Esta guía explica **paso a paso** cómo ejecutar el juego desde el navegador,
sin instalar nada. Hay dos caminos: **Codespaces** (recomendado, usa GitHub)
y **Trinket** (alternativa rápida sin cuenta de GitHub).

---

## Opción A — GitHub Codespaces (recomendada)

Necesitas una cuenta de GitHub. Los Codespaces personales tienen horas
gratuitas cada mes; para clase sobra.

### 1 · Abrir el codespace

1. Entra en el repo: https://github.com/maximofernandezriera/snake-turtle
2. Pulsa el botón verde **`<> Code`** → pestaña **Codespaces** →
   **`Create codespace on main`**.
3. Espera: la primera vez tarda **3-5 minutos** en construir el entorno
   (se instala el escritorio web). Las siguientes veces arranca en segundos.
4. Se abre VS Code en tu navegador. Cuando veas el explorador de archivos
   a la izquierda con `snake.py`, el codespace está listo.

### 2 · Abrir el escritorio web

El juego necesita una pantalla. El codespace trae un escritorio Linux
que se ve en otra pestaña del navegador:

1. En la parte inferior de VS Code, abre la pestaña **PORTS**
   (junto a TERMINAL). Si no aparece: `Ctrl+`` ` ` y en la barra de la
   terminal elige la pestaña **PORTS**.
2. Busca el puerto **6080** — aparecerá como "Escritorio web".
3. Pasa el ratón sobre la dirección y pulsa el icono del **mundo**
   ("Open in Browser") o copia la URL en una pestaña nueva.
4. Se abre una pantalla negra con un escritorio Linux. Si pide
   contraseña: **`vscode`**.

> ¿No ves el puerto 6080? Espera un minuto — el escritorio tarda un poco
> en levantarse. Si sigue sin aparecer, en TERMINAL escribe
> `/usr/local/desktop-lite/start-node-novnc.sh &` y refresca PORTS.

### 3 · Lanzar el juego

1. En VS Code web, abre un terminal: menú **Terminal → New Terminal**
   (o `` Ctrl+` ``).
2. Lanza el juego apuntando al escritorio web (su display es `:1`):

   ```bash
   DISPLAY=:1 python3 snake.py
   ```

   > Si algún día da `couldn't connect to display`: `ls /tmp/.X11-unix/`
   > te dice cuál hay (`X1` → `:1`, `X0` → `:0`).

3. **Cambia a la pestaña del escritorio web** (la del paso 2): ahí aparece
   la ventana negra del Snake.
4. Haz clic **dentro del escritorio web** para que el teclado llegue al juego.

### 4 · Jugar

- Flechas **↑ ↓ ← →** para dirigir la serpiente.
- No puedes dar media vuelta (sería chocarte contigo mismo).
- Para parar: cierra la ventana del juego desde el escritorio web, o en el
  terminal pulsa `Ctrl+C` y cierra la ventana con la X del escritorio.

### 5 · Terminar (importante)

Cuando acabes, para no gastar horas de codespace:

- GitHub → tu avatar → **Codespaces** → junto al codespace, `...` →
  **Stop codespace**. Si ya no lo necesitas, **Delete**.

### Problemas frecuentes en Codespaces

| Síntoma | Solución |
|---|---|
| El juego corre pero no se ve nada | Estás mirando VS Code: la ventana está en la **otra pestaña** (la del puerto 6080) |
| `ModuleNotFoundError: tkinter` | El codespace está viejo: bórralo y créalo de nuevo (el devcontainer lo instala solo) |
| `couldn't connect to display ":0"` | El display no es `:0`: mira `ls /tmp/.X11-unix/` y usa el número que salga (`DISPLAY=:1 python3 snake.py`) |
| El teclado no responde | Haz clic dentro del escritorio web; el foco debe estar en esa ventana |
| "No such file or directory: snake.py" | Estás en otra carpeta: `cd /workspaces/snake-turtle` |
| Puerto 6080 no aparece | Espera 1 min; o ejecuta `/usr/local/desktop-lite/start-node-novnc.sh &` |

---

## Opción B — Trinket (alternativa rápida)

Sin cuenta, sin esperas. Ideal si Codespaces falla o para un repaso rápido.

1. Abre https://trinket.io
2. Pulsa **Sign Up / Log In** (opcional) o directamente elige
   **New Trinket → Python** en el menú.
3. Borra el código de ejemplo.
4. En este repo, abre `snake.py`, cópialo **entero** y pégalo en Trinket.
5. Pulsa **Run**. La ventana del juego aparece en la propia página.
6. Mismas teclas: **flechas ↑ ↓ ← →**.

Ojo: en Trinket algunas teclas de flecha pueden reservarse para el
navegador; si falla, usa dos teclas letra (p. ej. cambia en el código
`"Up"` por `"i"` y `"Down"` por `"k"`) y añade:
`pantalla.onkey(der_arriba, "i")` / `pantalla.onkey(der_abajo, "k")`.

---

## Opción C — En tu equipo (si tienes Python instalado)

```bash
# descarga el repo o copia snake.py, luego:
python3 snake.py        # Windows: python snake.py
```

También desde IDLE (viene con Python) o Thonny: abrir `snake.py` y ejecutar.

---

## Para el docente — checklist de despliegue

Antes de la sesión (10 min):

- [ ] Entrar al repo y crear el codespace **antes de clase** para que la
      primera construcción no ocurra delante de los alumnos.
- [ ] Probar el flujo completo: PORTS → 6080 → escritorio →
      `DISPLAY=:0 python3 snake.py` → mover las palas.
- [ ] Dejar el codespace parado (**Stop**, no Delete): en clase arrancará
      en segundos con el entorno ya construido.
- [ ] Tener Trinket abierto en otra pestaña como plan B si Codespaces falla.
- [ ] Si los alumnos van a lanzarlo ellos: que sigan esta misma guía,
      Opción A si tienen cuenta de GitHub, Opción B si no.
- [ ] Proyector con la pizarra (`pizarra-snake.png`, repo `snake-docente`).

Recordatorio de coste: los codespaces facturan horas a la cuenta; para
enseñar en pantalla compartida basta **un solo codespace** — los alumnos
no necesitan abrir el suyo para ver la exposición.
