# 把 · Oración con 把
### Práctica de la oración con 把 (把字句) para hispanohablantes · 給西語學習者的把字句練習遊戲

🎮 **Jugar / 開始玩:** https://wangchiapin.github.io/practica-de-ba-oracion/

---

## 🇪🇸 Español

**把 (Oración con 把)** es un juego web para practicar la estructura **把** del chino mandarín. En cada pregunta ves dos imágenes, **antes** y **después**, y debes formar o reconocer la oración correcta.

> 誰 + **把** + 東西 + 動作 + 結果  
> Ejemplo: 我**把**書放在桌子上。 (Puse el libro sobre la mesa.)

### Cómo se juega
- En la **pantalla de inicio** (todo en una sola página) escribes tu **apodo** (obligatorio), eliges el nivel y juegas. Los textos de la interfaz se ven en dos líneas: chino grande y español/inglés pequeño.
- **3 niveles** con un banco de oraciones que sigue creciendo (cada partida elige 10 al azar):
  1. **關卡 1 · Nivel 1** – poner algo en un lugar (poner, colgar, pegar, meter, clavar/insertar, ponerse): 把書放在桌子上
  2. **關卡 2 · Nivel 2** – cómo queda algo (romper, limpiar, abrir/cerrar, encender/apagar, llenar/vaciar, borrar…): 他把杯子打破了
  3. **關卡 3 · Nivel 3** – dar, llevar o deshacerse de algo (dar, enviar, prestar, entregar, llevar a, mover a): 我把禮物送給朋友
- Cada nivel mezcla **3 tipos de pregunta**:
  - **Ordenar tarjetas**: mira las imágenes y ordena las palabras.
  - **Escuchar y elegir**: oye la oración (palabra por palabra) y elige la imagen de "después".
  - **Elegir la oración correcta** (al acertar, las opciones desaparecen y queda solo la oración, igual que en los otros dos tipos): una frase correcta y dos incorrectas (solo se usan errores que de verdad no se pueden decir, por ejemplo 把 mal colocado o sin el complemento final; nunca una frase natural sin 把).
- Los tres niveles también incluyen **oraciones negativas**: «沒把…» (no lo hice) y «別把…» (no lo hagas). En «沒把» la imagen del «después» es igual a la del «antes» con una ✕; en «別把» se dibuja el resultado con una ✕. Las oraciones con «別把» no salen en «Escuchar y elegir».
- Muchos objetos aparecen **en pareja**: el mismo objeto con resultados distintos (abrir/cerrar, ensuciar/limpiar, llenar/vaciar…), y en «Escuchar y elegir» la otra mitad de la pareja suele aparecer entre las opciones, así que hay que fijarse en la imagen del «después».
- Todas las imágenes están dibujadas con código (SVG), con un estilo sencillo y limpio.

### Puntos
| Acción | Puntos |
|---|---|
| Correcta a la primera | 100 (con racha ×1.2 y ×1.5) |
| Bonus de rapidez (primeros 10 s) | hasta +50 |
| Correcta en el segundo intento | 50 |
| Usar "Pista" (traducción) | −20 |
| Usar "Vocabulario" | sin penalización |

No hay vidas: el nivel termina tras 10 preguntas.
**Estrellas** según las respuestas correctas a la primera: 5+ → ★, 7+ → ★★, 9+ → ★★★.
Se necesita al menos ★ para desbloquear el siguiente nivel. Al final hay un **repaso de errores** (un botón que se abre solo si lo necesitas, para que no empuje el resto de la pantalla) y un **ranking** (mejor puntaje por jugador, top 10).

### Idiomas y lectura
- Interfaz en **Español / English / solo chino** (en "solo chino" no se ve ningún texto en español ni en inglés: sin traducciones ni significados; el botón "Pista" solo se ofrece en las preguntas de escuchar, donde muestra la oración escrita)
- Español de Latinoamérica (sin variante de España)
- Todo se cambia en el botón ⚙ (inicio, niveles y durante el juego). En el juego hay **pausa**, **reiniciar** y **menú**; reiniciar y volver al menú piden confirmación.
- Caracteres **繁體 / 简体**
- Lectura en **pinyin / zhuyin (注音) / ambos / sin lectura** (por defecto: pinyin), con **pronunciación de Taiwán** (según el Diccionario del Ministerio de Educación; con cambio de tono de 一/不)
- Voz en `zh-TW`, con tres velocidades: **lenta** (0.45), **normal** (0.65, por defecto) y **rápida** (0.85). En "escuchar y elegir", la oración se lee palabra por palabra a la velocidad elegida (la pausa entre palabras se ajusta a la velocidad).
- **Ajustes compartidos con los otros juegos:** caracteres, idioma, lectura y velocidad se guardan en `localStorage` bajo la clave `hanziGames.settings`, con la forma `{"v":1,"script":"trad|simp","lang":"es|en|zh","phon":"pinyin|zhuyin|both|off","rate":"slow|normal|fast"}`. Se comparten entre los juegos del mismo dominio y se sincronizan entre pestañas; los campos desconocidos que escriban otros juegos se conservan. Los ajustes antiguos de este juego (`ba_cfg`) se migran la primera vez. Nombre, progreso y ranking siguen guardándose solo en este juego.
- Botón **Vocabulario** en cada pregunta con significado, pinyin/zhuyin y audio de cada palabra (en "solo chino": palabra, lectura y audio)

### Para profesores
- Es un solo archivo: `index.html`. Funciona en GitHub Pages sin compilar nada.
- Los tres niveles están abiertos desde el principio (no hay desbloqueo).
- **Ranking compartido (Firebase Firestore):** ya está conectado al proyecto `memorma-24dab` (compartido con Memorama y Ordena el Armario), con inicio de sesión anónimo; los puntajes se guardan en la colección `baLeaderboard` (mejor puntaje de cada uno de los tres niveles, suma total, 10 mejores). La configuración está en `FIREBASE_CONFIG` de `index.html`; si no se puede conectar, el ranking solo se guarda en el dispositivo. Desde 2026-10-21 también se registran visitas, inicios y partidas terminadas (`visits` y `plays` del mismo proyecto; GA no cambia).
- **Modo clase (hecho; abrir/cerrar lo decide el interruptor del Centro de profesores):** si el enlace lleva `?class=` + código de clase (el profesor lo genera en el «Centro de profesores»), el resultado de cada nivel se envía al profesor: se guarda en `class_scores` del proyecto central `subscription-48d3c` (una entrada por alumno y por nivel, solo la mejor puntuación). El juego no tiene interruptor propio: todo lo decide el interruptor de mantenimiento del Centro de profesores (`portalStatus/center-ba`; sin documento = en mantenimiento, `off:false` = abierto). En mantenimiento, los enlaces de clase muestran «en mantenimiento», no se puede jugar y no se guardan resultados (`?preview` exceptuado). Sin `?class=` el juego funciona igual que siempre.
- **Reporte de preguntas:** el botón «🚩 Algo raro» (这题怪怪的) en cada pregunta envía el reporte (motivo, nota, imágenes, oración) a `game_reports` del proyecto central `subscription-48d3c` (`game:'ba'`); solo Ben lo ve, en «Problemas reportados» de `stats.html` del sitio de enlaces.
- **Vista previa al compartir:** `og.jpg` (1200×630) y las etiquetas `og:` del `<head>` (título «把 · oración con 把»).
- **GA4 (opcional):** escribe tu ID en `GA_ID`. Eventos: `ba_start`, `ba_level_start`, `ba_answer`, `ba_level_end`.
- Para agregar o editar oraciones, las oraciones nuevas van al final de `RAW3` (palabras con caracteres tradicionales, simplificados, pinyin y zhuyin) y se registran en cuatro tablas por número: `LV2` (nivel), `SPEC` (qué imagen dibujar), `KEYS` (objeto y lugar/resultado, para que las opciones de «Escuchar y elegir» no se parezcan demasiado) y `PATMAP` (tipo de errores para «Elegir la oración correcta»). Los significados van en `GLOSS3`. Las oraciones cuyas imágenes se parecen demasiado y no deben aparecer juntas en «Escuchar y elegir» se guardan en `SIMSET` (se genera comparando las imágenes; hay que volver a comprobarlo al agregar oraciones). Las imágenes se arman con piezas ya existentes (objetos `OB`, lugares `PL`, personas `PERS`, destinos `DS`).
- La carpeta `docs/` guarda la tabla de revisión de todas las oraciones (`把字句檢查表.csv`), la tabla de lecturas (`讀音總表.csv`) y las listas «para revisar» de cada tanda nueva.

---

## 🇹🇼 繁體中文

**把** 是一個練習「把字句」的網頁小遊戲。每題會看到「之前」和「之後」兩張圖，學生要排出或認出正確的句子。

> 誰 ＋ **把** ＋ 東西 ＋ 動作 ＋ 結果

### 玩法
- **首頁只有一頁**：輸入暱稱（必填）、選關卡、開始玩；介面文字分兩行，上面中文大字、下面西文／英文小字
- 共 **3 關**，題庫會持續增加（每次遊玩隨機抽 10 題）：關卡 1 是把東西放到某個地方（放、掛、貼、塞、插、戴）、關卡 2 是東西變成什麼樣子（打破、洗乾淨、打開／關上、倒滿／倒空、擦掉…）、關卡 3 是給人、送去或處理掉（給、寄、送、借、交、帶到、搬到）
- 每關混合三種題型：**排字卡**、**聽音選圖**、**選出正確的句子**（答對後選項會收起來，只留下句子，三種題型的答對畫面一致；錯誤選項只用真正不通順的句子，不會拿掉「把」變成另一種自然說法）
- 三個關卡裡也混了否定句「沒把…」和「別把…」：「沒把」的「之後」圖和「之前」一樣並打 ✕，「別把」畫出做了的結果並打 ✕；「別把」不出聽音選圖
- 很多東西會**成對出現**：同一個東西、不同結果（打開／關上、弄髒／洗乾淨、倒滿／倒空…）；聽音選圖時，成對的另一句常會出現在選項裡，要看「之後」的圖才分得出來
- 圖片全部用程式碼繪製，風格簡單乾淨

### 計分與結束
- 第一次答對 100 分，連續答對有加成（×1.2、×1.5）
- 10 秒內答對最多再加 50 分；第二次才答對得 50 分
- 看「提示」（整句翻譯）扣 20 分；查「詞彙」不扣分
- 不扣命，每關 10 題結束；依第一次就答對的題數給 1～3 顆星
- 結算有**錯題複習**（收成一個按鈕，要看再點開，錯很多題時不會把下面的按鈕推到很底下），另有**排行榜**（每人只留最高分，前 10 名）

### 語言與讀音
- 介面：Español／English／只有中文（「只有中文」不會出現任何西文或英文，沒有翻譯和詞義；「提示」只在聽音題提供，顯示整句文字）
- 西班牙文統一使用拉丁美洲用法
- 字體：繁體／简体
- 讀音：拼音／注音／兩個都顯示／不顯示（預設拼音），**以台灣讀音為主**（依教育部《國語辭典》，含一、不變調）
- 設定都在右上角 ⚙；遊戲中有暫停、重新開始、選單（重新開始和回選單會先確認；暫停會停止計時）
- 西班牙文統一用拉丁美洲用法
- 語音使用 `zh-TW`，三種語速：慢 0.45、中 0.65（預設）、快 0.85；聽音題逐詞念，用你選的語速，詞與詞之間的停頓會跟著語速調整
- **和其他遊戲共用設定**：字體、介面語言、讀音、語速存在 `localStorage` 的 `hanziGames.settings`，格式 `{"v":1,"script":"trad|simp","lang":"es|en|zh","phon":"pinyin|zhuyin|both|off","rate":"slow|normal|fast"}`；同網域的遊戲互通、分頁之間即時同步，其他遊戲多存的欄位會保留。舊版的 `ba_cfg` 設定第一次開啟時會自動搬過來。名字、進度和排行榜仍只存在這個遊戲。
- 每題都有「詞彙」按鈕，可查每個詞的拼音、注音、意思（西文／英文），並聽發音；「只有中文」時只顯示詞、讀音和發音

### 老師設定
- 單一檔案 `index.html`，放在 GitHub Pages 即可使用
- 三個關卡一開始就全部開放（沒有解鎖機制）
- 排行榜已接到 Firebase 專案 `memorma-24dab`（與翻牌記憶、收納小達人共用，匿名登入，集合 `baLeaderboard`，前 10 名）；設定在 `index.html` 的 `FIREBASE_CONFIG`，連不上時只存在該裝置
- 2026-10-21 起也記錄訪客、開始、玩完（同專案的 `visits`、`plays`，GA 不動）
- **班級模式（已做好，開不開放由老師管理中心的維修開關決定）**：連結帶 `?class=班級碼`（老師在「老師管理中心」產生）時，每關成績會回傳給老師，存到中央專案 `subscription-48d3c` 的 `class_scores`（每位學生每一關一筆，只留最高分）。遊戲本身沒有自己的開關，全由老師管理中心的維修開關（`portalStatus/center-ba`，沒有設定＝預設維修中、`off:false`＝開放）決定：維修中時老師中心的卡片變淡、班級連結顯示「🔧 維修中」不能玩也不記成績（`?preview` 例外）。沒有 `?class=` 時遊戲跟原來一樣
- **題目回報**：每題有「🚩 這題怪怪的」按鈕，送出（原因、備註、圖、題目句）到中央專案 `subscription-48d3c` 的 `game_reports`（`game:'ba'`）；只有 Ben 在分享區 `stats.html` 的「問題回報」看得到
- **分享連結預覽**：`og.jpg`（1200×630）加 `<head>` 裡的 og 標籤（標題「把 · oración con 把」）
- 可選擇填入 `GA_ID` 啟用 GA4
- 新增或修改句子：新句子加在 `RAW3` 最後面，再依編號登記到 `LV2`（第幾關）、`SPEC`（要畫什麼圖）、`KEYS`（東西＋地點或結果，讓聽音題的選項不會太像）、`PATMAP`（選句子題的錯誤句型），詞義加在 `GLOSS3`；聽音題「圖片太像、不要同時出現」的句子記在 `SIMSET`（用圖片逐格比對產生），新增句子後要重新比對；圖用現成的物品（`OB`）、地點（`PL`）、人物（`PERS`）、目的地（`DS`）組起來
- `docs/` 資料夾放全部句子的檢查表（`把字句檢查表.csv`）、讀音總表（`讀音總表.csv`）和每一批新句子的審查表

---

由「每天一分鐘 · 一分鐘學中文」製作 · Hecho por Ben (@cadadiaunosminutos_ben_chino)

## 手機瀏覽器備註：捲動後回不到頂端（2026-10-24）
iPhone 版 Chrome 上，頁面可以捲動時，往下捲之後有時回不到最上面（Safari 正常）。
處理方式（已套用在本遊戲）：
- `<meta name="viewport">` 設 `maximum-scale=1`，不使用 `viewport-fit=cover`。
- `<html>` 加 `html{color-scheme:light}`。

兩項一起改後，手機 Chrome 測試恢復正常；尚未分開測是哪一項有效。新增頁面請照這個寫。

## 測試

`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 tests/test_game.py`（Python + Playwright；擋掉外部網路，用假的 Firebase 和假的語音，不碰真的資料庫）

- 目前 144 項檢查（2026-10-30 建立）。
- 涵蓋：維修開關（`portalStatus/center-ba`）、`?preview`、`?class=`、三關全開、整關解題、計分（第二次答對 50、兩次錯 0、提示 −20）、星等門檻（5／7／9 題）、設定每個值、公開排行榜、班級成績、題目回報。與「被」是同一套程式的測試。
- 改了遊戲的計分、設定、排行榜或畫面文字後，推上去之前先跑一次。
- 驗證方式：另外複製一份遊戲、故意改壞一個地方，測試會出現 FAIL。
