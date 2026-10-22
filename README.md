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
- **371 oraciones en 3 niveles** (cada partida elige 10 al azar):
  1. **關卡 1 · Nivel 1** – poner algo en un lugar: 把書放在桌子上
  2. **關卡 2 · Nivel 2** – cómo queda algo: 他把杯子打破了
  3. **關卡 3 · Nivel 3** – dar, llevar o deshacerse de algo: 我把禮物送給朋友
- Cada nivel mezcla **3 tipos de pregunta**:
  - **Ordenar tarjetas**: mira las imágenes y ordena las palabras.
  - **Escuchar y elegir**: oye la oración (palabra por palabra) y elige la imagen de "después".
  - **Elegir la oración correcta** (al acertar, las opciones desaparecen y queda solo la oración, igual que en los otros dos tipos): una frase correcta y dos incorrectas (solo se usan errores que de verdad no se pueden decir, por ejemplo 把 mal colocado o sin el complemento final; nunca una frase natural sin 把).
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
- Para modo de prueba con todos los niveles abiertos: añade `?unlock=1` a la URL.
- **Ranking compartido (Firebase Firestore):** ya está conectado al proyecto `memorma-24dab` (compartido con Memorama y Ordena el Armario), con inicio de sesión anónimo; los puntajes se guardan en la colección `baLeaderboard` (mejor puntaje de cada uno de los tres niveles, suma total, 10 mejores). La configuración está en `FIREBASE_CONFIG` de `index.html`; si no se puede conectar, el ranking solo se guarda en el dispositivo. Desde 2026-10-21 también se registran visitas, inicios y partidas terminadas (`visits` y `plays` del mismo proyecto; GA no cambia).
- **GA4 (opcional):** escribe tu ID en `GA_ID`. Eventos: `ba_start`, `ba_level_start`, `ba_answer`, `ba_level_end`.
- Para agregar o editar oraciones, modifica el arreglo `RAW` (palabras con caracteres tradicionales, simplificados, pinyin y zhuyin), el diccionario `GLOSS` (significados) y el dibujo correspondiente en `SC`.

---

## 🇹🇼 繁體中文

**把** 是一個練習「把字句」的網頁小遊戲。每題會看到「之前」和「之後」兩張圖，學生要排出或認出正確的句子。

> 誰 ＋ **把** ＋ 東西 ＋ 動作 ＋ 結果

### 玩法
- **首頁只有一頁**：輸入暱稱（必填）、選關卡、開始玩；介面文字分兩行，上面中文大字、下面西文／英文小字
- 共 **371 句、3 關**（第 1 關 129、第 2 關 127、第 3 關 115）（每次遊玩隨機抽 10 題）：關卡 1 是把東西放到某個地方、關卡 2 是東西變成什麼樣子、關卡 3 是給人、送去或處理掉
- 每關混合三種題型：**排字卡**、**聽音選圖**、**選出正確的句子**（答對後選項會收起來，只留下句子，三種題型的答對畫面一致；錯誤選項只用真正不通順的句子，不會拿掉「把」變成另一種自然說法）
- 圖片全部用程式碼繪製，風格簡單乾淨

### 計分與結束
- 第一次答對 100 分，連續答對有加成（×1.2、×1.5）
- 10 秒內答對最多再加 50 分；第二次才答對得 50 分
- 看「提示」（整句翻譯）扣 20 分；查「詞彙」不扣分
- 不扣命，每關 10 題結束；依第一次就答對的題數給 1～3 顆星，至少 1 顆星才能解鎖下一關
- 結算有**錯題複習**（收成一個按鈕，要看再點開，錯很多題時不會把下面的按鈕推到很底下），另有**排行榜**（每人只留最高分，前 10 名）

### 語言與讀音
- 介面：Español／English／只有中文（「只有中文」不會出現任何西文或英文，沒有翻譯和詞義；「提示」只在聽音題提供，顯示整句文字）
- 西班牙文版本：拉丁美洲／西班牙（用詞不同，例如 carro／coche、celular／móvil、piso／suelo），只在介面為西文時顯示
- 字體：繁體／简体
- 讀音：拼音／注音／兩個都顯示／不顯示（預設拼音），**以台灣讀音為主**（依教育部《國語辭典》，含一、不變調）
- 設定都在右上角 ⚙；遊戲中有暫停、重新開始、選單（重新開始和回選單會先確認；暫停會停止計時）
- 西班牙文統一用拉丁美洲用法
- 語音使用 `zh-TW`，三種語速：慢 0.45、中 0.65（預設）、快 0.85；聽音題逐詞念，用你選的語速，詞與詞之間的停頓會跟著語速調整
- **和其他遊戲共用設定**：字體、介面語言、讀音、語速存在 `localStorage` 的 `hanziGames.settings`，格式 `{"v":1,"script":"trad|simp","lang":"es|en|zh","phon":"pinyin|zhuyin|both|off","rate":"slow|normal|fast"}`；同網域的遊戲互通、分頁之間即時同步，其他遊戲多存的欄位會保留。舊版的 `ba_cfg` 設定第一次開啟時會自動搬過來。名字、進度和排行榜仍只存在這個遊戲。
- 每題都有「詞彙」按鈕，可查每個詞的拼音、注音、意思（西文／英文），並聽發音；「只有中文」時只顯示詞、讀音和發音

### 老師設定
- 單一檔案 `index.html`，放在 GitHub Pages 即可使用
- 測試時在網址後面加 `?unlock=1` 可解鎖全部關卡
- 排行榜已接到 Firebase 專案 `memorma-24dab`（與翻牌記憶、收納小達人共用，匿名登入，集合 `baLeaderboard`，前 10 名）；設定在 `index.html` 的 `FIREBASE_CONFIG`，連不上時只存在該裝置
- 2026-10-21 起也記錄訪客、開始、玩完（同專案的 `visits`、`plays`，GA 不動）
- 可選擇填入 `GA_ID` 啟用 GA4

---

由「每天一分鐘 · 一分鐘學中文」製作 · Hecho por Ben (@cadadiaunosminutos_ben_chino)
