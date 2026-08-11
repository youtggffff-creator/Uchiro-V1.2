# 🇰🇭 Uchiro Store — Telegram Bot

Bot នេះមាន **២ (+១ Optional)** ដាច់ដោយឡែក ប៉ុន្តែ share database ដូចគ្នា:

1. **Admin Bot** (`admin_bot.py`) — សម្រាប់ Uchiro (ម្ចាស់ហាង/Seller) ប្រើបន្ថែម/កែ/លុប stock, Code, Guide, វិធាន
2. **Store Bot** (`store_bot.py`) — សម្រាប់អតិថិជនមើលទំនិញ និងទិញ
3. **Helper Bot** (`helper_bot.py`, Optional) — Bot ជំនួយឥតគិតថ្លៃសម្រាប់អ្នកលេង Blox Fruits ដែលផ្សព្វផ្សាយទៅកាន់ Store Bot

ទាំងអស់អាចដំណើរការជាមួយគ្នាតាមរយៈ `main.py` (ដំណើរការ process តែមួយ) ។ Helper Bot ចាប់ផ្តើមតែពេលកំណត់ `HELPER_BOT_TOKEN` ប៉ុណ្ណោះ។

---

## ១. បង្កើត Bot ក្នុង Telegram

1. បើក Telegram ស្វែងរក **@BotFather**
2. `/newbot` → ដាក់ឈ្មោះ Admin Bot → ទទួល **Token** ទី ១
3. `/newbot` → ដាក់ឈ្មោះ Store Bot → ទទួល **Token** ទី ២
4. (Optional) `/newbot` → ដាក់ឈ្មោះ Helper Bot → ទទួល **Token** ទី ៣

## ២. រកលេខ Telegram Chat ID (Admin)

ស្វែងរក **@userinfobot** → Start → ចម្លងលេខ `Id:`

## ៣. ដំឡើងកម្មវិធី

```bash
cd uchiro_store_bot
pip install -r requirements.txt
```

## ៤. កំណត់ Token និង Owner ID

```bash
export ADMIN_BOT_TOKEN="123456:AAA-your-admin-bot-token"
export STORE_BOT_TOKEN="789012:BBB-your-store-bot-token"
export OWNER_IDS="123456789"
export STORE_BOT_USERNAME="UchiroStoreBot"
```

Owner អាចបន្ថែម Admin/អ្នកលក់ថ្មីលើ Bot ដោយប្រើ `/addseller` — មិនចាំបាច់កែ config ទេ។
📞 លេខ Contact Admin (`@noreakyout`), Channel (`t.me/uchirostore`), Video Creator credit កំណត់នៅ `config.py`។

## ៥. ដំណើរការ

```bash
python main.py
```

---

## របៀបប្រើ — Admin Bot

**📦 Account (មានរូបភាព, ១មុខម្តង):**
- `/additem` — ប្រភេទ → ឈ្មោះ → តម្លៃ → ពិពណ៌នា → ស្តុក → ព័ត៌មានគណនី → រូបភាព

**⚡ Fruit/Gamepass/Evade/Robux/Blade Ball/MM2 (លឿន, ច្រើនក្នុងម្តងតែម្តង):**
- `/addstock` — ជ្រើសរើសប្រភេទ (ប៊ូតុង) រួចវាយ `ឈ្មោះ, តម្លៃ, ស្តុក` ១បន្ទាត់=១មុខ (ច្រើនបន្ទាត់ម្តងបាន)
- `/addfruit`, `/addgamepass` — Shortcut ដូច `/addstock` ប៉ុន្តែរំលងជំហានជ្រើសប្រភេទ
- `/setstock <id> <ចំនួន>` — កែស្តុកលឿន
- `/setprice <id> <តម្លៃ>` — កែតម្លៃលឿន
- `/cancel` — បោះបង់ Flow កំពុងធ្វើ

**🎮 ជួយ Player:**
- `/setcodes` — Update Redeem Code ថ្មី (`/codes` សម្រាប់ Player)
- `/settierlist` — Update Fruit Tier List (`/tierlist` សម្រាប់ Player, គាំទ្រ `*Bold*`)
- `/addguide ចំណងជើង | Link YouTube` — បន្ថែម Video Guide (`/guide` សម្រាប់ Player)
- `/removeguide <id>`, `/guides` — គ្រប់គ្រង Guide

**📜 វិធាន:**
- `/setrules` — កែវិធាន/Warranty (`/rules` សម្រាប់ Player)

**🛠 គ្រប់គ្រង:**
- `/listitems` — មើល/កែ/លុប ទំនិញ (មាន ID សម្រាប់ `/setstock`, `/setprice`)
- `/orders` — Order កំពុងរង់ចាំ — ✅ អនុម័ត / ❌ បដិសេធ (អនុម័តរួច Bot ផ្ញើគណនីទៅអតិថិជនស្វ័យប្រវត្តិ ហើយកាត់ស្តុក)
- `/setpayment`, `/showpayment` — QR + ព័ត៌មានទូទាត់
- `/stats`, `/users` — ស្ថិតិ + បញ្ជីអ្នកប្រើប្រាស់

**👑 Owner ប៉ុណ្ណោះ:**
- `/addseller <telegram_id>`, `/removeseller <telegram_id>`, `/sellers`

## របៀបប្រើ — Store Bot (អតិថិជន)

- `/start` — មើលប្រភេទទំនិញ + ប៊ូតុង 📞 ទាក់ទងម្ចាស់ហាង
- `/support` — ទាក់ទងម្ចាស់ហាងផ្ទាល់
- `/codes`, `/tierlist`, `/guide` — ជំនួយ Player
- `/rules` — វិធាន/Warranty
- ជ្រើសរើសប្រភេទ → **Account**: card រូបភាពដាច់ដោយឡែក — **ផ្សេងទៀត**: បញ្ជីស្តុករួម (Option 1, 2, 3...)
- ចុច "🛍 ទិញឥឡូវ" → Bot បង្ហាញ QR + តម្លៃ → ✅ បញ្ជាក់ / ❌ បោះបង់ → ផ្ញើ Screenshot ទូទាត់ → Order ចូល Admin ភ្លាមៗ

## 🛍 Mini App (Store UI ថ្មី — Premium Look)

`webapp_server.py` + `webapp/templates/index.html` = Telegram Mini App ពិតប្រាកដ (Search, Filter តម្លៃ, Category Tab, Warranty Badge, Animation Gear 5 theme) ។

**ការកំណត់:**
1. Deploy `main.py` ដូចធម្មតា — Web Server ចាប់ផ្តើមស្វ័យប្រវត្តិនៅពេលកំណត់ `WEBAPP_URL`
2. `WEBAPP_URL` ត្រូវជា HTTPS URL សាធារណៈពិតប្រាកដ (Railway ឲ្យ URL បែបនេះដោយស្វ័យប្រវត្តិ — មើលក្នុង Settings → Networking → Generate Domain)
3. កំណត់ Environment Variables បន្ថែម:

| Key | Value |
|---|---|
| `WEBAPP_URL` | `https://your-app.up.railway.app` |
| `STORE_BOT_USERNAME` | username Store Bot គ្មាន @ |

4. Restart → `/start` លើ Store Bot នឹងបង្ហាញប៊ូតុង "✨ បើក Uchiro Store App" ដោយស្វ័យប្រវត្តិ (ឬប្រើ `/shop`)

**របៀបដំណើរការ:** Mini App ជា UI សម្រាប់ Browse/Search/Filter ប៉ុណ្ណោះ — ពេលអតិថិជនចុច "ទិញឥឡូវ" ក្នុង App វានឹង Deep-link ត្រឡប់ទៅ Chat Bot ដើម្បីបន្ត Flow ទូទាត់ (QR + Screenshot + Admin អនុម័ត) ដដែល — មិនមានហានិភ័យទិន្នន័យទូទាត់កាន់តាមផ្នែក Web ទេ។

**Warranty Badge:** បង្ហាញស្វ័យប្រវត្តិ "🛡️ 14ថ្ងៃ" លើ Card ណាដែលជា Category "Account" ។

## របៀបប្រើ — Helper Bot (Optional)

- `/start`, `/codes`, `/tierlist`, `/guide` — ដូច Store Bot ប៉ុន្តែផ្តោតលើជំនួយ Player
- រាល់ចម្លើយមាន Credit ទៅកាន់ម្ចាស់ Video (`CREATOR_NAME` ក្នុង `config.py`) + ប៊ូតុងនាំទៅ Store Bot

---

## សំខាន់! Telegram file_id មិនចម្លងគ្នារវាង Bot បានទេ

រូបភាពទាំងអស់ (item, QR, payment screenshot) ត្រូវរក្សាទុកនៅ folder **`media/`** ក្បែរ `store.db` ជានិច្ច (ប្រព័ន្ធទាញយករូបភាពមកផ្ទុកលើ Server ផ្ទាល់ រួចផ្ញើពី disk វិញ ដើម្បីចៀសវាង `Wrong file identifier` error)។ Backup ត្រូវចម្លងទាំង `store.db` និង `media/`។

## Troubleshooting

- **ប៊ូតុងចុចមិនដំណើរការ / Bot ស្ងាត់**: ភាគច្រើនបណ្តាលមកពី **រត់ instance ២ ក្នុងពេលតែមួយ** ដោយប្រើ Token ដដែល (`Conflict: terminated by other getUpdates request`) — ត្រូវប្រាកដថារត់តែកន្លែងតែមួយ
- **`OWNER_IDS`** ត្រូវជាលេខ Telegram ID មិនមែន username
- Token របស់ Bot នីមួយៗត្រូវខុសគ្នា
