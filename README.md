# 把它放好 · Ponlo en su lugar
### Práctica de la oración con 把 (把字句) para hispanohablantes · 給西語學習者的把字句練習遊戲

🎮 **Jugar / 開始玩:** https://wangchiapin.github.io/practica-de-ba-oracion/

---

## 🇪🇸 Español

**Ponlo en su lugar** es un juego web para practicar la estructura **把** del chino mandarín. En cada pregunta ves dos imágenes, **antes** y **después**, y debes formar o reconocer la oración correcta.

> 誰 + **把** + 東西 + 動作 + 結果  
> Ejemplo: 我**把**書放在桌子上。 (Puse el libro sobre la mesa.)

### Cómo se juega
- **30 oraciones en 3 niveles** (10 por nivel):
  1. **放置類 · Colocar cosas** – 把書放在桌子上
  2. **結果類 · Resultados** – 他把杯子打破了
  3. **處置類 · Dar y transformar** – 我把禮物送給朋友
- Cada nivel mezcla **3 tipos de pregunta**:
  - **Ordenar tarjetas**: mira las imágenes y ordena las palabras.
  - **Escuchar y elegir**: oye la oración (palabra por palabra) y elige la imagen de "después".
  - **Elegir la oración correcta**: una frase correcta y dos incorrectas (solo se usan errores que de verdad no se pueden decir, por ejemplo 把 mal colocado o sin el complemento final; nunca una frase natural sin 把).
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
Se necesita al menos ★ para desbloquear el siguiente nivel. Al final hay un **repaso de errores** y un **ranking** (mejor puntaje por jugador, top 15).

### Idiomas y lectura
- Interfaz en **Español / English**
- Variante del español: **Latinoamérica / España** (carro/coche, celular/móvil, tarea/deberes, pastel/tarta, piso/suelo…)
- Caracteres **繁體 / 简体**
- Lectura en **pinyin / zhuyin (注音) / sin lectura**, con **pronunciación de Taiwán** (según el Diccionario del Ministerio de Educación; con cambio de tono de 一/不)
- Voz en `zh-TW`, con velocidad **lenta** (por defecto) o normal
- Botón **Vocabulario** en cada pregunta con significado, pinyin/zhuyin y audio de cada palabra

### Para profesores
- Es un solo archivo: `index.html`. Funciona en GitHub Pages sin compilar nada.
- Para modo de prueba con todos los niveles abiertos: añade `?unlock=1` a la URL.
- **Ranking compartido (Firebase Firestore):** en `index.html` reemplaza `FIREBASE_CONFIG` por la configuración de tu proyecto. Los puntajes se guardan en la colección `baLeaderboard`. Sin configurar, el ranking solo se guarda en el dispositivo.
- **GA4 (opcional):** escribe tu ID en `GA_ID`. Eventos: `ba_start`, `ba_level_start`, `ba_answer`, `ba_level_end`.
- Para agregar o editar oraciones, modifica el arreglo `RAW` (palabras con caracteres tradicionales, simplificados, pinyin y zhuyin), el diccionario `GLOSS` (significados) y el dibujo correspondiente en `SC`.

---

## 🇹🇼 繁體中文

**把它放好** 是一個練習「把字句」的網頁小遊戲。每題會看到「之前」和「之後」兩張圖，學生要排出或認出正確的句子。

> 誰 ＋ **把** ＋ 東西 ＋ 動作 ＋ 結果

### 玩法
- 共 **30 句、3 關**，每關 10 題：放置類、結果類、處置類
- 每關混合三種題型：**排字卡**、**聽音選圖**、**選出正確的句子**（錯誤選項只用真正不通順的句子，不會拿掉「把」變成另一種自然說法）
- 圖片全部用程式碼繪製，風格簡單乾淨

### 計分與結束
- 第一次答對 100 分，連續答對有加成（×1.2、×1.5）
- 10 秒內答對最多再加 50 分；第二次才答對得 50 分
- 看「提示」（整句翻譯）扣 20 分；查「詞彙」不扣分
- 不扣命，每關 10 題結束；依第一次就答對的題數給 1～3 顆星，至少 1 顆星才能解鎖下一關
- 結算有**錯題複習**，另有**排行榜**（每人只留最高分，前 15 名）

### 語言與讀音
- 介面：Español / English
- 西班牙文版本：拉丁美洲／西班牙（用詞不同，例如 carro／coche、celular／móvil、piso／suelo）
- 字體：繁體／简体
- 讀音：拼音／注音／不顯示，**以台灣讀音為主**（依教育部《國語辭典》，含一、不變調）
- 語音使用 `zh-TW`，預設慢速，聽音題逐詞念
- 每題都有「詞彙」按鈕，可查每個詞的拼音、注音、西文與英文意思，並聽發音

### 老師設定
- 單一檔案 `index.html`，放在 GitHub Pages 即可使用
- 測試時在網址後面加 `?unlock=1` 可解鎖全部關卡
- 排行榜要共用，請把 `FIREBASE_CONFIG` 換成自己的 Firebase 設定（集合名稱：`baLeaderboard`）；沒設定時只存在該裝置
- 可選擇填入 `GA_ID` 啟用 GA4

---

由「每天一分鐘 · 一分鐘學中文」製作 · Hecho por Ben (@cadadiaunosminutos_ben_chino)
