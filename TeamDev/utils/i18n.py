"""
           ───── ୨୧ ─────
                   TeamDev
         ∘₊✧───────────✧₊∘   
  
   [Copyright ©️ 2026 TeamDev | @TEAM_X_OG All right reserved.]

Project Name: All In One Downloader
Project Discription: Download From Multiple Platforms Video Such As Terabox, Youtube, instagram, and much more!
Project Number: 38
Project By: @MR_ARMAN_08 | @TEAM_X_OG

                   Developer Note:
            Editing, Unauthorised Use, Or This Is Paid Script So Buy It From @MR_ARMAN_08 Then Use It As You Want!
"""


STRINGS: dict[str, dict[str, str]] = {

    "en": {        "start_caption": (            "◆ Welcome, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — Universal Media Downloader\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Pinterest\n"
            "▸ Terabox  ▸ Vimeo  ▸ SoundCloud  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "Built by {team_name}  ·  Dev: {dev_name}\n"
            "<i>Issues? Contact @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ Download",        "btn_help":         "◆ Help",        "btn_premium":      "★ Premium",        "btn_referral":     "◇ Referral",        "btn_language":     "◈ Language",        "help_text": (            "◆ Help Guide\n"
            "━━━━━━━━━━━━\n"
            "▸ Tap Download, choose platform, send link\n"
            "▸ Or send any supported link directly\n\n"
            "◆ Daily Limit: <code>{limit}</code> downloads\n"
            "◆ Refer friends → earn bonus downloads\n"
            "◆ Upgrade to Premium for unlimited access\n\n"
            "━━━━━━━━━━━━\n"
            "<i>Support: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev Premium\n"
            "━━━━━━━━━━━━\n"
            "▸ Unlimited Downloads\n"
            "▸ Zero Cooldown\n"
            "▸ No Force-Join\n"
            "▸ Ad-Free Experience\n"
            "▸ Priority Support\n"
            "━━━━━━━━━━━━\n"
            "Contact @MR_ARMAN_08 to upgrade."
        ),
        "referral_text": (            "◇ Your Referral Link\n"
            "━━━━━━━━━━━━\n"
            "<code>{ref_link}</code>\n\n"
            "◆ Points earned: {points}\n"
            "▸ 1 referral = 1 bonus download"
        ),
        "force_join": (            "◆ Channel Required\n\n"
            "▸ Join our channel to use this bot.\n"
            "▸ Then press /start again."
        ),
        "limit_reached": (            "◆ Daily Limit Reached\n\n"
            "▸ You've used all {limit} downloads today.\n"
            "▸ Refer friends or upgrade to Premium."
        ),
        "banned_msg": (            "◆ Access Denied\n\n"
            "▸ You have been banned from this bot.\n"
            "▸ Contact @MR_ARMAN_08 to appeal."
        ),
        "choose_platform": (            "◆ Select Platform\n\n"
            "<i>Choose where to download from:</i>"
        ),
        "platform_selected": (            "◆ {platform} Selected\n\n"
            "<i>Send the {platform} link now:</i>"
        ),
        "fetching": "◆ Fetching from {platform}...\n<i>Please wait.</i>",        "auto_detected": "◆ Auto-detected: {platform}\n<i>Fetching...</i>",        "download_ready": (            "◆ Download Ready\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}"
            "{quality_line}"
            "{duration_line}"
            "{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>Link valid for ~20 minutes</i>"
        ),
        "btn_download_file": "▸ Download File",        "invalid_url":    "◆ Invalid URL\n<i>Please send a supported link.</i>",        "error_generic":  "◆ Something went wrong\n<i>Please try again later.</i>\n<code>{err}</code>",        "lang_set":       "◆ Language set to English.",        "choose_lang":    "◆ Select Language\n<i>Choose your preferred language:</i>",        "downloads_left": "◇ {left} downloads remaining today.",        "ad_label":       "◆ — Sponsored —",        "admin_welcome":  "◆ Admin Panel\n<i>Select an action:</i>",        "setting_saved":  "◆ Setting saved.",        "ad_created":     "◆ Ad created and activated.",        "broadcast_done": "◆ Broadcast sent to {count} users.",        "limit_updated":  "◆ Daily limit updated to {limit}.",        "not_admin":      "◆ Access Denied\n<i>You are not authorised.</i>",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "hi": {        "start_caption": (            "◆ Swagat hai, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — Universal Media Downloader\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Pinterest\n"
            "▸ Terabox  ▸ Vimeo  ▸ SoundCloud  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "Banaya: {team_name}  ·  Dev: {dev_name}\n"
            "<i>Madad ke liye @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ Download",        "btn_help":         "◆ Sahayata",        "btn_premium":      "★ Premium",        "btn_referral":     "◇ Referral",        "btn_language":     "◈ Bhasha",        "help_text": (            "◆ Sahayata\n"
            "━━━━━━━━━━━━\n"
            "▸ Download dabao, platform chuno, link bhejo\n"
            "▸ Ya seedha supported link bhejein\n\n"
            "◆ Daily Limit: <code>{limit}</code> downloads\n"
            "◆ Dosto ko refer karo → bonus downloads\n"
            "◆ Premium mein unlimited access\n\n"
            "<i>Support: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev Premium\n"
            "━━━━━━━━━━━━\n"
            "▸ Unlimited Downloads\n"
            "▸ Koi Cooldown Nahi\n"
            "▸ Force-Join Nahi\n"
            "▸ Ads-Free\n"
            "▸ Priority Support\n"
            "━━━━━━━━━━━━\n"
            "Upgrade ke liye @MR_ARMAN_08 se sampark karein."
        ),
        "referral_text": (            "◇ Aapka Referral Link\n"
            "━━━━━━━━━━━━\n"
            "<code>{ref_link}</code>\n\n"
            "◆ Earned Points: {points}\n"
            "▸ 1 Referral = 1 Bonus Download"
        ),
        "force_join": (            "◆ Channel Zaruri Hai\n\n"
            "▸ Bot use karne ke liye channel join karein.\n"
            "▸ Phir /start dabayein."
        ),
        "limit_reached": (            "◆ Aaj Ki Limit Khatam\n\n"
            "▸ Aaj ke {limit} downloads use ho gaye.\n"
            "▸ Refer karein ya Premium upgrade karein."
        ),
        "banned_msg": (            "◆ Access Denied\n\n"
            "▸ Aapko ban kar diya gaya hai.\n"
            "▸ Appeal ke liye @MR_ARMAN_08 se sampark karein."
        ),
        "choose_platform": "◆ Platform Chunein\n\n<i>Kahan se download karna hai:</i>",        "platform_selected": "◆ {platform} Chuna Gaya\n\n<i>{platform} link bhejein:</i>",        "fetching": "◆ {platform} se la raha hoon...\n<i>Thoda intezaar karein.</i>",        "auto_detected": "◆ Auto-detect: {platform}\n<i>Fetch ho raha hai...</i>",        "download_ready": (            "◆ Download Taiyar\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}"
            "{quality_line}"
            "{duration_line}"
            "{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>Link ~20 minutes mein expire hoga</i>"
        ),
        "btn_download_file": "▸ File Download Karein",        "invalid_url":    "◆ Galat URL\n<i>Sahi supported link bhejein.</i>",        "error_generic":  "◆ Kuch Galat Hua\n<i>Baad mein dobara koshish karein.</i>\n<code>{err}</code>",        "lang_set":       "◆ Bhasha Hindi set kar di gayi.",        "choose_lang":    "◆ Bhasha Chunein",        "downloads_left": "◇ Aaj {left} downloads bache hain.",        "ad_label":       "◆ — Vigyapan —",        "admin_welcome":  "◆ Admin Panel",        "setting_saved":  "◆ Setting save ho gayi.",        "ad_created":     "◆ Ad create ho gayi.",        "broadcast_done": "◆ {count} users ko bheja.",        "limit_updated":  "◆ Daily limit {limit} set ki gayi.",        "not_admin":      "◆ Access Denied\n<i>Aap authorized nahi hain.</i>",                            "spotify_fetching": "◆ Spotify track aa raha hai...\n<i>MP3 download ho raha hai.</i>",        "spotify_sending": "◆ Audio file bheja ja raha hai...\n<i>Ek second ruko.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Sirf <b>track</b> links supported hain.\n▸ Albums/playlists abhi nahi.",    },

    "ru": {        "start_caption": (            "◆ Добро пожаловать, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — Универсальный загрузчик\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Pinterest\n"
            "▸ Terabox  ▸ Vimeo  ▸ SoundCloud  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "Создан: {team_name}  ·  Dev: {dev_name}\n"
            "<i>Помощь: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ Скачать",        "btn_help":         "◆ Помощь",        "btn_premium":      "★ Премиум",        "btn_referral":     "◇ Реферал",        "btn_language":     "◈ Язык",        "help_text": (            "◆ Справка\n"
            "━━━━━━━━━━━━\n"
            "▸ Нажмите Скачать, выберите платформу\n"
            "▸ Или сразу отправьте ссылку\n\n"
            "◆ Дневной лимит: <code>{limit}</code>\n"
            "◆ Приглашайте друзей → бонусные загрузки\n\n"
            "<i>Поддержка: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev Премиум\n"
            "━━━━━━━━━━━━\n"
            "▸ Безлимитные загрузки\n"
            "▸ Без задержек\n"
            "▸ Без рекламы\n"
            "▸ Приоритетная поддержка\n"
            "━━━━━━━━━━━━\n"
            "Написать @MR_ARMAN_08 для апгрейда."
        ),
        "referral_text": (            "◇ Ваша реферальная ссылка\n"
            "━━━━━━━━━━━━\n"
            "<code>{ref_link}</code>\n\n"
            "◆ Очки: {points}\n"
            "▸ 1 реферал = 1 бонусная загрузка"
        ),
        "force_join":     "◆ Требуется подписка\n\n▸ Вступите в канал.\n▸ Затем нажмите /start.",        "limit_reached":  "◆ Лимит исчерпан\n\n▸ Использовано {limit} загрузок.\n▸ Пригласите друзей или обновитесь.",        "banned_msg":     "◆ Доступ закрыт\n\n▸ Вы заблокированы.\n▸ Обратитесь в @MR_ARMAN_08.",        "choose_platform": "◆ Выберите платформу",        "platform_selected": "◆ {platform} выбран\n\n<i>Отправьте ссылку {platform}:</i>",        "fetching":        "◆ Загрузка из {platform}...",        "auto_detected":   "◆ Определено: {platform}\n<i>Загружаю...</i>",        "download_ready": (            "◆ Готово к скачиванию\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>Ссылка действует ~20 минут</i>"
        ),
        "btn_download_file": "▸ Скачать файл",        "invalid_url":    "◆ Неверная ссылка",        "error_generic":  "◆ Ошибка\n<i>Попробуйте позже.</i>\n<code>{err}</code>",        "lang_set":       "◆ Язык: Русский.",        "choose_lang":    "◆ Выберите язык",        "downloads_left": "◇ Осталось {left} загрузок.",        "ad_label":       "◆ — Реклама —",        "admin_welcome":  "◆ Панель администратора",        "setting_saved":  "◆ Настройка сохранена.",        "ad_created":     "◆ Объявление создано.",        "broadcast_done": "◆ Отправлено {count} пользователям.",        "limit_updated":  "◆ Лимит: {limit}.",        "not_admin":      "◆ Нет доступа",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "ar": {        "start_caption": (            "◆ أهلاً {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — محمّل الوسائط الشامل\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "طُوِّر بواسطة {team_name}\n"
            "<i>للمساعدة: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ تحميل",        "btn_help":         "◆ مساعدة",        "btn_premium":      "★ مميز",        "btn_referral":     "◇ إحالة",        "btn_language":     "◈ اللغة",        "help_text": (            "◆ دليل الاستخدام\n"
            "━━━━━━━━━━━━\n"
            "▸ اضغط تحميل، اختر المنصة، أرسل الرابط\n"
            "▸ أو أرسل الرابط مباشرةً\n\n"
            "◆ الحد اليومي: <code>{limit}</code> تحميلات\n"
            "◆ ادعُ أصدقاءك → تحميلات إضافية\n\n"
            "<i>الدعم: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev مميز\n"
            "━━━━━━━━━━━━\n"
            "▸ تحميلات غير محدودة\n"
            "▸ بدون إعلانات\n"
            "▸ دعم أولوية\n"
            "━━━━━━━━━━━━\n"
            "تواصل مع @MR_ARMAN_08 للترقية."
        ),
        "referral_text": (            "◇ رابط الإحالة الخاص بك\n"
            "━━━━━━━━━━━━\n"
            "<code>{ref_link}</code>\n\n"
            "◆ النقاط: {points}\n"
            "▸ إحالة واحدة = تحميل إضافي"
        ),
        "force_join":     "◆ انضمام مطلوب\n\n▸ انضم إلى قناتنا لاستخدام البوت.\n▸ ثم اضغط /start.",        "limit_reached":  "◆ وصلت للحد اليومي\n\n▸ استخدمت كل {limit} تحميلات.\n▸ ادعُ أصدقاء أو قم بالترقية.",        "banned_msg":     "◆ وصول مرفوض\n\n▸ تم حظرك.\n▸ تواصل مع @MR_ARMAN_08.",        "choose_platform": "◆ اختر المنصة",        "platform_selected": "◆ {platform} محدد\n\n<i>أرسل رابط {platform}:</i>",        "fetching":        "◆ جارٍ الجلب من {platform}...",        "auto_detected":   "◆ تم الكشف: {platform}\n<i>جارٍ التحميل...</i>",        "download_ready": (            "◆ جاهز للتحميل\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>الرابط صالح لـ ~20 دقيقة</i>"
        ),
        "btn_download_file": "▸ تحميل الملف",        "invalid_url":    "◆ رابط غير صحيح",        "error_generic":  "◆ حدث خطأ\n<i>حاول مجدداً.</i>\n<code>{err}</code>",        "lang_set":       "◆ اللغة: العربية.",        "choose_lang":    "◆ اختر اللغة",        "downloads_left": "◇ {left} تحميلات متبقية اليوم.",        "ad_label":       "◆ — إعلان —",        "admin_welcome":  "◆ لوحة الإدارة",        "setting_saved":  "◆ تم الحفظ.",        "ad_created":     "◆ تم إنشاء الإعلان.",        "broadcast_done": "◆ أُرسل إلى {count} مستخدم.",        "limit_updated":  "◆ الحد اليومي: {limit}.",        "not_admin":      "◆ وصول مرفوض",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "es": {        "start_caption": (            "◆ Bienvenido, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — Descargador Universal\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "Por {team_name}  ·  Dev: {dev_name}\n"
            "<i>Ayuda: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ Descargar",        "btn_help":         "◆ Ayuda",        "btn_premium":      "★ Premium",        "btn_referral":     "◇ Referido",        "btn_language":     "◈ Idioma",        "help_text": (            "◆ Guía de Uso\n"
            "━━━━━━━━━━━━\n"
            "▸ Toca Descargar, elige plataforma, envía enlace\n"
            "▸ O envía el enlace directamente\n\n"
            "◆ Límite diario: <code>{limit}</code>\n\n"
            "<i>Soporte: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev Premium\n"
            "━━━━━━━━━━━━\n"
            "▸ Descargas ilimitadas\n"
            "▸ Sin anuncios\n"
            "▸ Soporte prioritario\n"
            "━━━━━━━━━━━━\n"
            "Contacta @MR_ARMAN_08 para mejorar."
        ),
        "referral_text":   "◇ Tu enlace de referido\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ Puntos: {points}",        "force_join":      "◆ Canal requerido\n\n▸ Únete al canal.\n▸ Luego presiona /start.",        "limit_reached":   "◆ Límite alcanzado\n\n▸ Usaste {limit} descargas hoy.\n▸ Refiere amigos o actualiza.",        "banned_msg":      "◆ Acceso denegado\n\n▸ Has sido baneado.\n▸ Contacta @MR_ARMAN_08.",        "choose_platform": "◆ Selecciona plataforma",        "platform_selected": "◆ {platform} seleccionado\n\n<i>Envía el enlace de {platform}:</i>",        "fetching":         "◆ Obteniendo de {platform}...",        "auto_detected":    "◆ Detectado: {platform}\n<i>Descargando...</i>",        "download_ready": (            "◆ Listo para descargar\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>Enlace válido ~20 minutos</i>"
        ),
        "btn_download_file": "▸ Descargar Archivo",        "invalid_url":    "◆ URL inválida",        "error_generic":  "◆ Algo salió mal\n<code>{err}</code>",        "lang_set":       "◆ Idioma: Español.",        "choose_lang":    "◆ Selecciona idioma",        "downloads_left": "◇ {left} descargas restantes.",        "ad_label":       "◆ — Patrocinado —",        "admin_welcome":  "◆ Panel Admin",        "setting_saved":  "◆ Configuración guardada.",        "ad_created":     "◆ Anuncio creado.",        "broadcast_done": "◆ Enviado a {count} usuarios.",        "limit_updated":  "◆ Límite: {limit}.",        "not_admin":      "◆ Acceso denegado",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "pt": {        "start_caption": (            "◆ Bem-vindo, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — Baixador Universal de Mídia\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "Por {team_name}  ·  Dev: {dev_name}\n"
            "<i>Suporte: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ Baixar",        "btn_help":         "◆ Ajuda",        "btn_premium":      "★ Premium",        "btn_referral":     "◇ Indicação",        "btn_language":     "◈ Idioma",        "help_text": (            "◆ Guia de Uso\n"
            "━━━━━━━━━━━━\n"
            "▸ Toque em Baixar, escolha a plataforma\n"
            "▸ Ou envie o link diretamente\n\n"
            "◆ Limite diário: <code>{limit}</code>\n\n"
            "<i>Suporte: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev Premium\n"
            "━━━━━━━━━━━━\n"
            "▸ Downloads ilimitados\n"
            "▸ Sem anúncios\n"
            "▸ Suporte prioritário\n"
            "━━━━━━━━━━━━\n"
            "Contate @MR_ARMAN_08 para assinar."
        ),
        "referral_text":   "◇ Seu link de indicação\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ Pontos: {points}",        "force_join":      "◆ Canal necessário\n\n▸ Entre no canal.\n▸ Depois pressione /start.",        "limit_reached":   "◆ Limite atingido\n\n▸ Você usou {limit} downloads hoje.\n▸ Indique amigos ou assine Premium.",        "banned_msg":      "◆ Acesso negado\n\n▸ Você foi banido.\n▸ Contate @MR_ARMAN_08.",        "choose_platform": "◆ Selecione a plataforma",        "platform_selected": "◆ {platform} selecionado\n\n<i>Envie o link do {platform}:</i>",        "fetching":         "◆ Buscando de {platform}...",        "auto_detected":    "◆ Detectado: {platform}\n<i>Baixando...</i>",        "download_ready": (            "◆ Pronto para baixar\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>Link válido por ~20 minutos</i>"
        ),
        "btn_download_file": "▸ Baixar Arquivo",        "invalid_url":    "◆ URL inválida",        "error_generic":  "◆ Algo deu errado\n<code>{err}</code>",        "lang_set":       "◆ Idioma: Português.",        "choose_lang":    "◆ Selecione o idioma",        "downloads_left": "◇ {left} downloads restantes.",        "ad_label":       "◆ — Patrocinado —",        "admin_welcome":  "◆ Painel Admin",        "setting_saved":  "◆ Configuração salva.",        "ad_created":     "◆ Anúncio criado.",        "broadcast_done": "◆ Enviado para {count} usuários.",        "limit_updated":  "◆ Limite: {limit}.",        "not_admin":      "◆ Acesso negado",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "fr": {        "start_caption": (            "◆ Bienvenue, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — Téléchargeur Universel\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "Par {team_name}  ·  Dev: {dev_name}\n"
            "<i>Aide: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ Télécharger",        "btn_help":         "◆ Aide",        "btn_premium":      "★ Premium",        "btn_referral":     "◇ Parrainage",        "btn_language":     "◈ Langue",        "help_text": (            "◆ Guide d'utilisation\n"
            "━━━━━━━━━━━━\n"
            "▸ Appuyez Télécharger, choisissez plateforme\n"
            "▸ Ou envoyez directement le lien\n\n"
            "◆ Limite quotidienne: <code>{limit}</code>\n\n"
            "<i>Support: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev Premium\n"
            "━━━━━━━━━━━━\n"
            "▸ Téléchargements illimités\n"
            "▸ Sans publicité\n"
            "▸ Support prioritaire\n"
            "━━━━━━━━━━━━\n"
            "Contactez @MR_ARMAN_08 pour mettre à niveau."
        ),
        "referral_text":   "◇ Votre lien de parrainage\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ Points: {points}",        "force_join":      "◆ Rejoindre le canal requis\n\n▸ Rejoignez notre canal.\n▸ Puis appuyez /start.",        "limit_reached":   "◆ Limite atteinte\n\n▸ Vous avez utilisé {limit} téléchargements.\n▸ Parrainez des amis ou passez Premium.",        "banned_msg":      "◆ Accès refusé\n\n▸ Vous êtes banni.\n▸ Contactez @MR_ARMAN_08.",        "choose_platform": "◆ Choisissez la plateforme",        "platform_selected": "◆ {platform} sélectionné\n\n<i>Envoyez le lien {platform}:</i>",        "fetching":         "◆ Récupération depuis {platform}...",        "auto_detected":    "◆ Détecté: {platform}\n<i>Téléchargement...</i>",        "download_ready": (            "◆ Prêt à télécharger\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>Lien valide ~20 minutes</i>"
        ),
        "btn_download_file": "▸ Télécharger le fichier",        "invalid_url":    "◆ URL invalide",        "error_generic":  "◆ Une erreur est survenue\n<code>{err}</code>",        "lang_set":       "◆ Langue: Français.",        "choose_lang":    "◆ Choisissez la langue",        "downloads_left": "◇ {left} téléchargements restants.",        "ad_label":       "◆ — Sponsorisé —",        "admin_welcome":  "◆ Panneau Admin",        "setting_saved":  "◆ Paramètre enregistré.",        "ad_created":     "◆ Annonce créée.",        "broadcast_done": "◆ Envoyé à {count} utilisateurs.",        "limit_updated":  "◆ Limite: {limit}.",        "not_admin":      "◆ Accès refusé",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "id": {        "start_caption": (            "◆ Selamat datang, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — Pengunduh Media Universal\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "Oleh {team_name}  ·  Dev: {dev_name}\n"
            "<i>Bantuan: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ Unduh",        "btn_help":         "◆ Bantuan",        "btn_premium":      "★ Premium",        "btn_referral":     "◇ Referral",        "btn_language":     "◈ Bahasa",        "help_text": (            "◆ Panduan Penggunaan\n"
            "━━━━━━━━━━━━\n"
            "▸ Ketuk Unduh, pilih platform, kirim tautan\n"
            "▸ Atau kirim tautan langsung\n\n"
            "◆ Batas harian: <code>{limit}</code>\n\n"
            "<i>Dukungan: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev Premium\n"
            "━━━━━━━━━━━━\n"
            "▸ Unduhan tak terbatas\n"
            "▸ Tanpa iklan\n"
            "▸ Dukungan prioritas\n"
            "━━━━━━━━━━━━\n"
            "Hubungi @MR_ARMAN_08 untuk upgrade."
        ),
        "referral_text":   "◇ Tautan referral Anda\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ Poin: {points}",        "force_join":      "◆ Bergabung diperlukan\n\n▸ Gabung channel kami.\n▸ Lalu tekan /start.",        "limit_reached":   "◆ Batas tercapai\n\n▸ Anda telah menggunakan {limit} unduhan.\n▸ Referensikan teman atau upgrade.",        "banned_msg":      "◆ Akses ditolak\n\n▸ Anda telah diblokir.\n▸ Hubungi @MR_ARMAN_08.",        "choose_platform": "◆ Pilih Platform",        "platform_selected": "◆ {platform} dipilih\n\n<i>Kirim tautan {platform}:</i>",        "fetching":         "◆ Mengambil dari {platform}...",        "auto_detected":    "◆ Terdeteksi: {platform}\n<i>Mengunduh...</i>",        "download_ready": (            "◆ Siap diunduh\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>Tautan valid ~20 menit</i>"
        ),
        "btn_download_file": "▸ Unduh File",        "invalid_url":    "◆ URL tidak valid",        "error_generic":  "◆ Terjadi kesalahan\n<code>{err}</code>",        "lang_set":       "◆ Bahasa: Indonesia.",        "choose_lang":    "◆ Pilih Bahasa",        "downloads_left": "◇ {left} unduhan tersisa hari ini.",        "ad_label":       "◆ — Disponsori —",        "admin_welcome":  "◆ Panel Admin",        "setting_saved":  "◆ Pengaturan disimpan.",        "ad_created":     "◆ Iklan dibuat.",        "broadcast_done": "◆ Terkirim ke {count} pengguna.",        "limit_updated":  "◆ Batas: {limit}.",        "not_admin":      "◆ Akses ditolak",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "bn": {        "start_caption": (            "◆ স্বাগতম, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — সর্বজনীন মিডিয়া ডাউনলোডার\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "তৈরি: {team_name}  ·  Dev: {dev_name}\n"
            "<i>সহায়তা: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ ডাউনলোড",        "btn_help":         "◆ সাহায্য",        "btn_premium":      "★ প্রিমিয়াম",        "btn_referral":     "◇ রেফারেল",        "btn_language":     "◈ ভাষা",        "help_text": (            "◆ সাহায্য\n"
            "━━━━━━━━━━━━\n"
            "▸ ডাউনলোড চাপুন, প্ল্যাটফর্ম বেছে নিন\n"
            "▸ অথবা সরাসরি লিঙ্ক পাঠান\n\n"
            "◆ দৈনিক সীমা: <code>{limit}</code>\n\n"
            "<i>সহায়তা: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev প্রিমিয়াম\n"
            "━━━━━━━━━━━━\n"
            "▸ সীমাহীন ডাউনলোড\n"
            "▸ কোনো বিজ্ঞাপন নেই\n"
            "▸ অগ্রাধিকার সহায়তা\n"
            "━━━━━━━━━━━━\n"
            "@MR_ARMAN_08-এ যোগাযোগ করুন।"
        ),
        "referral_text":   "◇ আপনার রেফারেল লিঙ্ক\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ পয়েন্ট: {points}",        "force_join":      "◆ চ্যানেলে যোগ দিন\n\n▸ চ্যানেলে যোগ দিন।\n▸ তারপর /start চাপুন।",        "limit_reached":   "◆ দৈনিক সীমা শেষ\n\n▸ আজকের {limit} ডাউনলোড শেষ।\n▸ রেফার করুন বা প্রিমিয়াম নিন।",        "banned_msg":      "◆ প্রবেশ নিষিদ্ধ",        "choose_platform": "◆ প্ল্যাটফর্ম বেছে নিন",        "platform_selected": "◆ {platform} বেছে নেওয়া হয়েছে\n\n<i>{platform} লিঙ্ক পাঠান:</i>",        "fetching":         "◆ {platform} থেকে আনা হচ্ছে...",        "auto_detected":    "◆ শনাক্ত: {platform}",        "download_ready": (            "◆ ডাউনলোড প্রস্তুত\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>লিঙ্ক ~২০ মিনিট বৈধ</i>"
        ),
        "btn_download_file": "▸ ফাইল ডাউনলোড",        "invalid_url":    "◆ অবৈধ URL",        "error_generic":  "◆ সমস্যা হয়েছে\n<code>{err}</code>",        "lang_set":       "◆ ভাষা: বাংলা।",        "choose_lang":    "◆ ভাষা বেছে নিন",        "downloads_left": "◇ আজ {left} ডাউনলোড বাকি।",        "ad_label":       "◆ — বিজ্ঞাপন —",        "admin_welcome":  "◆ অ্যাডমিন প্যানেল",        "setting_saved":  "◆ সংরক্ষিত।",        "ad_created":     "◆ বিজ্ঞাপন তৈরি।",        "broadcast_done": "◆ {count} জনকে পাঠানো হয়েছে।",        "limit_updated":  "◆ সীমা: {limit}।",        "not_admin":      "◆ প্রবেশ নিষিদ্ধ",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "tr": {        "start_caption": (            "◆ Hoş geldin, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — Evrensel Medya İndirici\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "Yapan: {team_name}  ·  Dev: {dev_name}\n"
            "<i>Yardım: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ İndir",        "btn_help":         "◆ Yardım",        "btn_premium":      "★ Premium",        "btn_referral":     "◇ Referans",        "btn_language":     "◈ Dil",        "help_text": (            "◆ Kullanım Kılavuzu\n"
            "━━━━━━━━━━━━\n"
            "▸ İndir'e dokun, platform seç, link gönder\n"
            "▸ Ya da linki doğrudan gönder\n\n"
            "◆ Günlük limit: <code>{limit}</code>\n\n"
            "<i>Destek: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev Premium\n"
            "━━━━━━━━━━━━\n"
            "▸ Sınırsız indirme\n"
            "▸ Reklamsız\n"
            "▸ Öncelikli destek\n"
            "━━━━━━━━━━━━\n"
            "Yükseltmek için @MR_ARMAN_08'e yaz."
        ),
        "referral_text":   "◇ Referans linkin\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ Puan: {points}",        "force_join":      "◆ Kanal gerekli\n\n▸ Kanala katıl.\n▸ Sonra /start'a bas.",        "limit_reached":   "◆ Limit doldu\n\n▸ {limit} indirme hakkın bitti.\n▸ Arkadaş davet et veya Premium al.",        "banned_msg":      "◆ Erişim reddedildi",        "choose_platform": "◆ Platform seç",        "platform_selected": "◆ {platform} seçildi\n\n<i>{platform} linkini gönder:</i>",        "fetching":         "◆ {platform}'dan alınıyor...",        "auto_detected":    "◆ Tespit edildi: {platform}",        "download_ready": (            "◆ İndirmeye hazır\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>Link ~20 dakika geçerli</i>"
        ),
        "btn_download_file": "▸ Dosyayı İndir",        "invalid_url":    "◆ Geçersiz URL",        "error_generic":  "◆ Bir hata oluştu\n<code>{err}</code>",        "lang_set":       "◆ Dil: Türkçe.",        "choose_lang":    "◆ Dil seç",        "downloads_left": "◇ Bugün {left} indirme hakkın kaldı.",        "ad_label":       "◆ — Reklam —",        "admin_welcome":  "◆ Admin Paneli",        "setting_saved":  "◆ Ayar kaydedildi.",        "ad_created":     "◆ Reklam oluşturuldu.",        "broadcast_done": "◆ {count} kullanıcıya gönderildi.",        "limit_updated":  "◆ Limit: {limit}.",        "not_admin":      "◆ Erişim reddedildi",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "ta": {        "start_caption": (            "◆ வரவேற்கிறோம், {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — யூனிவர்சல் மீடியா டவுன்லோடர்\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "உருவாக்கியவர்: {team_name}  ·  Dev: {dev_name}\n"
            "<i>உதவி: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ பதிவிறக்கு",        "btn_help":         "◆ உதவி",        "btn_premium":      "★ பிரீமியம்",        "btn_referral":     "◇ ரெஃபரல்",        "btn_language":     "◈ மொழி",        "help_text": (            "◆ உதவி\n"
            "━━━━━━━━━━━━\n"
            "▸ பதிவிறக்கு அழுத்து, தளம் தேர்வு செய், இணைப்பு அனுப்பு\n"
            "▸ அல்லது நேரடியாக இணைப்பு அனுப்பு\n\n"
            "◆ தினசரி வரம்பு: <code>{limit}</code>\n\n"
            "<i>ஆதரவு: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev பிரீமியம்\n"
            "━━━━━━━━━━━━\n"
            "▸ வரம்பற்ற பதிவிறக்கங்கள்\n"
            "▸ விளம்பரம் இல்லை\n"
            "▸ முன்னுரிமை ஆதரவு\n"
            "━━━━━━━━━━━━\n"
            "தொடர்பு: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ உங்கள் ரெஃபரல் இணைப்பு\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ புள்ளிகள்: {points}",        "force_join":      "◆ சேனல் தேவை\n\n▸ சேனலில் சேரவும்.\n▸ பின் /start அழுத்தவும்.",        "limit_reached":   "◆ தினசரி வரம்பு முடிந்தது\n\n▸ {limit} பதிவிறக்கங்கள் முடிந்தன.",        "banned_msg":      "◆ அணுகல் மறுக்கப்பட்டது",        "choose_platform": "◆ தளம் தேர்வு செய்யவும்",        "platform_selected": "◆ {platform} தேர்ந்தெடுக்கப்பட்டது\n\n<i>{platform} இணைப்பு அனுப்பவும்:</i>",        "fetching":         "◆ {platform}-லிருந்து கொண்டு வருகிறோம்...",        "auto_detected":    "◆ கண்டறியப்பட்டது: {platform}",        "download_ready": (            "◆ பதிவிறக்கம் தயார்\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>இணைப்பு ~20 நிமிடங்கள் செல்லுபடியாகும்</i>"
        ),
        "btn_download_file": "▸ கோப்பை பதிவிறக்கு",        "invalid_url":    "◆ தவறான URL",        "error_generic":  "◆ பிழை ஏற்பட்டது\n<code>{err}</code>",        "lang_set":       "◆ மொழி: தமிழ்.",        "choose_lang":    "◆ மொழி தேர்வு செய்யவும்",        "downloads_left": "◇ இன்று {left} பதிவிறக்கங்கள் மீதமுள்ளன.",        "ad_label":       "◆ — விளம்பரம் —",        "admin_welcome":  "◆ நிர்வாக பேனல்",        "setting_saved":  "◆ அமைப்பு சேமிக்கப்பட்டது.",        "ad_created":     "◆ விளம்பரம் உருவாக்கப்பட்டது.",        "broadcast_done": "◆ {count} பயனர்களுக்கு அனுப்பப்பட்டது.",        "limit_updated":  "◆ வரம்பு: {limit}.",        "not_admin":      "◆ அணுகல் மறுக்கப்பட்டது",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "te": {        "start_caption": (            "◆ స్వాగతం, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — యూనివర్సల్ మీడియా డౌన్‌లోడర్\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "నిర్మించినది: {team_name}  ·  Dev: {dev_name}\n"
            "<i>సహాయం: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ డౌన్‌లోడ్",        "btn_help":         "◆ సహాయం",        "btn_premium":      "★ ప్రీమియం",        "btn_referral":     "◇ రెఫెరల్",        "btn_language":     "◈ భాష",        "help_text": (            "◆ సహాయం\n"
            "━━━━━━━━━━━━\n"
            "▸ డౌన్‌లోడ్ నొక్కు, వేదిక ఎంచుకో, లింక్ పంపు\n"
            "▸ లేదా నేరుగా లింక్ పంపు\n\n"
            "◆ రోజువారీ పరిమితి: <code>{limit}</code>\n\n"
            "<i>సహాయం: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev ప్రీమియం\n"
            "━━━━━━━━━━━━\n"
            "▸ అపరిమిత డౌన్‌లోడ్లు\n"
            "▸ ప్రకటనలు లేవు\n"
            "▸ ప్రాధాన్య మద్దతు\n"
            "━━━━━━━━━━━━\n"
            "సంప్రదించండి: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ మీ రెఫెరల్ లింక్\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ పాయింట్లు: {points}",        "force_join":      "◆ ఛానెల్ అవసరం\n\n▸ ఛానెల్‌లో చేరండి.\n▸ తర్వాత /start నొక్కండి.",        "limit_reached":   "◆ రోజువారీ పరిమితి అయిపోయింది\n\n▸ {limit} డౌన్‌లోడ్లు అయిపోయాయి.",        "banned_msg":      "◆ యాక్సెస్ తిరస్కరించబడింది",        "choose_platform": "◆ వేదిక ఎంచుకోండి",        "platform_selected": "◆ {platform} ఎంచుకోబడింది\n\n<i>{platform} లింక్ పంపండి:</i>",        "fetching":         "◆ {platform} నుండి తెస్తున్నాము...",        "auto_detected":    "◆ గుర్తించబడింది: {platform}",        "download_ready": (            "◆ డౌన్‌లోడ్ సిద్ధం\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>లింక్ ~20 నిమిషాలు చెల్లుతుంది</i>"
        ),
        "btn_download_file": "▸ ఫైల్ డౌన్‌లోడ్",        "invalid_url":    "◆ చెల్లని URL",        "error_generic":  "◆ లోపం సంభవించింది\n<code>{err}</code>",        "lang_set":       "◆ భాష: తెలుగు.",        "choose_lang":    "◆ భాష ఎంచుకోండి",        "downloads_left": "◇ ఈరోజు {left} డౌన్‌లోడ్లు మిగిలాయి.",        "ad_label":       "◆ — ప్రకటన —",        "admin_welcome":  "◆ అడ్మిన్ ప్యానెల్",        "setting_saved":  "◆ సెట్టింగ్ సేవ్ అయింది.",        "ad_created":     "◆ ప్రకటన సృష్టించబడింది.",        "broadcast_done": "◆ {count} వినియోగదారులకు పంపబడింది.",        "limit_updated":  "◆ పరిమితి: {limit}.",        "not_admin":      "◆ యాక్సెస్ తిరస్కరించబడింది",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "mr": {        "start_caption": (            "◆ स्वागत आहे, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — युनिव्हर्सल मीडिया डाउनलोडर\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "बनवले: {team_name}  ·  Dev: {dev_name}\n"
            "<i>मदतीसाठी: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ डाउनलोड",        "btn_help":         "◆ मदत",        "btn_premium":      "★ प्रीमियम",        "btn_referral":     "◇ रेफरल",        "btn_language":     "◈ भाषा",        "help_text": (            "◆ मदत\n"
            "━━━━━━━━━━━━\n"
            "▸ डाउनलोड दाबा, प्लॅटफॉर्म निवडा, लिंक पाठवा\n"
            "▸ किंवा थेट लिंक पाठवा\n\n"
            "◆ दैनिक मर्यादा: <code>{limit}</code>\n\n"
            "<i>सहाय्य: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev प्रीमियम\n"
            "━━━━━━━━━━━━\n"
            "▸ अमर्यादित डाउनलोड\n"
            "▸ जाहिरात नाही\n"
            "▸ प्राधान्य सहाय्य\n"
            "━━━━━━━━━━━━\n"
            "संपर्क करा: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ तुमची रेफरल लिंक\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ गुण: {points}",        "force_join":      "◆ चॅनेल आवश्यक\n\n▸ चॅनेलमध्ये सामील व्हा.\n▸ नंतर /start दाबा.",        "limit_reached":   "◆ दैनिक मर्यादा संपली\n\n▸ {limit} डाउनलोड संपले.",        "banned_msg":      "◆ प्रवेश नाकारला",        "choose_platform": "◆ प्लॅटफॉर्म निवडा",        "platform_selected": "◆ {platform} निवडले\n\n<i>{platform} लिंक पाठवा:</i>",        "fetching":         "◆ {platform} वरून आणत आहे...",        "auto_detected":    "◆ ओळखले: {platform}",        "download_ready": (            "◆ डाउनलोड तयार\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>लिंक ~20 मिनिटे वैध</i>"
        ),
        "btn_download_file": "▸ फाईल डाउनलोड",        "invalid_url":    "◆ अवैध URL",        "error_generic":  "◆ काहीतरी चुकले\n<code>{err}</code>",        "lang_set":       "◆ भाषा: मराठी.",        "choose_lang":    "◆ भाषा निवडा",        "downloads_left": "◇ आज {left} डाउनलोड शिल्लक.",        "ad_label":       "◆ — जाहिरात —",        "admin_welcome":  "◆ Admin Panel",        "setting_saved":  "◆ सेटिंग जतन केली.",        "ad_created":     "◆ जाहिरात तयार केली.",        "broadcast_done": "◆ {count} वापरकर्त्यांना पाठवले.",        "limit_updated":  "◆ मर्यादा: {limit}.",        "not_admin":      "◆ प्रवेश नाकारला",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "gu": {        "start_caption": (            "◆ સ્વાગત છે, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — યુનિવર્સલ મીડિયા ડાઉનલોડર\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "બનાવ્યું: {team_name}  ·  Dev: {dev_name}\n"
            "<i>મદદ: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ ડાઉનલોડ",        "btn_help":         "◆ મદદ",        "btn_premium":      "★ પ્રીમિયમ",        "btn_referral":     "◇ રેફરલ",        "btn_language":     "◈ ભાષા",        "help_text": (            "◆ મદદ\n"
            "━━━━━━━━━━━━\n"
            "▸ ડાઉનલોડ દબાવો, પ્લેટફોર્મ પસંદ કરો, લિંક મોકલો\n"
            "▸ અથવા સીધી લિંક મોકલો\n\n"
            "◆ દૈનિક મર્યાદા: <code>{limit}</code>\n\n"
            "<i>સહાય: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev પ્રીમિયમ\n"
            "━━━━━━━━━━━━\n"
            "▸ અમર્યાદિત ડાઉનલોડ\n"
            "▸ જાહેરાત નહીં\n"
            "▸ પ્રાથમિક સહાય\n"
            "━━━━━━━━━━━━\n"
            "સંપર્ક: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ તમારી રેફરલ લિંક\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ પોઈન્ટ: {points}",        "force_join":      "◆ ચેનલ જરૂરી\n\n▸ ચેનલ જોઈન કરો.\n▸ પછી /start દબાવો.",        "limit_reached":   "◆ દૈનિક મર્યાદા પૂરી\n\n▸ {limit} ડાઉનલોડ વપરાઈ ગઈ.",        "banned_msg":      "◆ એક્સેસ નામંજૂર",        "choose_platform": "◆ પ્લેટફોર્મ પસંદ કરો",        "platform_selected": "◆ {platform} પસંદ\n\n<i>{platform} લિંક મોકલો:</i>",        "fetching":         "◆ {platform} માંથી લઈ રહ્યા છીએ...",        "auto_detected":    "◆ ઓળખ્યું: {platform}",        "download_ready": (            "◆ ડાઉનલોડ તૈયાર\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>લિંક ~20 મિનિટ માટે માન્ય</i>"
        ),
        "btn_download_file": "▸ ફાઇલ ડાઉનલોડ",        "invalid_url":    "◆ અમાન્ય URL",        "error_generic":  "◆ ભૂલ આવી\n<code>{err}</code>",        "lang_set":       "◆ ભાષા: ગુજરાતી.",        "choose_lang":    "◆ ભાષા પસંદ કરો",        "downloads_left": "◇ આજે {left} ડાઉનલોડ બાકી.",        "ad_label":       "◆ — જાહેરાત —",        "admin_welcome":  "◆ Admin Panel",        "setting_saved":  "◆ સેટિંગ સેવ.",        "ad_created":     "◆ જાહેરાત બની.",        "broadcast_done": "◆ {count} વપરાશકર્તાઓને મોકલ્યું.",        "limit_updated":  "◆ મર્યાદા: {limit}.",        "not_admin":      "◆ એક્સેસ નામંજૂર",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "kn": {        "start_caption": (            "◆ ಸ್ವಾಗತ, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — ಯೂನಿವರ್ಸಲ್ ಮೀಡಿಯಾ ಡೌನ್‌ಲೋಡರ್\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "ನಿರ್ಮಿಸಿದ್ದು: {team_name}  ·  Dev: {dev_name}\n"
            "<i>ಸಹಾಯ: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ ಡೌನ್‌ಲೋಡ್",        "btn_help":         "◆ ಸಹಾಯ",        "btn_premium":      "★ ಪ್ರೀಮಿಯಂ",        "btn_referral":     "◇ ರೆಫರಲ್",        "btn_language":     "◈ ಭಾಷೆ",        "help_text": (            "◆ ಸಹಾಯ\n"
            "━━━━━━━━━━━━\n"
            "▸ ಡೌನ್‌ಲೋಡ್ ಒತ್ತು, ವೇದಿಕೆ ಆರಿಸು, ಲಿಂಕ್ ಕಳಿಸು\n"
            "▸ ಅಥವಾ ನೇರವಾಗಿ ಲಿಂಕ್ ಕಳಿಸು\n\n"
            "◆ ದೈನಿಕ ಮಿತಿ: <code>{limit}</code>\n\n"
            "<i>ಬೆಂಬಲ: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev ಪ್ರೀಮಿಯಂ\n"
            "━━━━━━━━━━━━\n"
            "▸ ಅಪರಿಮಿತ ಡೌನ್‌ಲೋಡ್\n"
            "▸ ಜಾಹೀರಾತು ಇಲ್ಲ\n"
            "▸ ಆದ್ಯತೆ ಬೆಂಬಲ\n"
            "━━━━━━━━━━━━\n"
            "ಸಂಪರ್ಕಿಸಿ: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ ನಿಮ್ಮ ರೆಫರಲ್ ಲಿಂಕ್\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ ಪಾಯಿಂಟ್ಗಳು: {points}",        "force_join":      "◆ ಚಾನೆಲ್ ಅಗತ್ಯ\n\n▸ ಚಾನೆಲ್ ಸೇರಿ.\n▸ ನಂತರ /start ಒತ್ತಿ.",        "limit_reached":   "◆ ದೈನಿಕ ಮಿತಿ ಮುಗಿದಿದೆ\n\n▸ {limit} ಡೌನ್‌ಲೋಡ್ ಮುಗಿದಿದೆ.",        "banned_msg":      "◆ ಪ್ರವೇಶ ನಿರಾಕರಿಸಲಾಗಿದೆ",        "choose_platform": "◆ ವೇದಿಕೆ ಆರಿಸಿ",        "platform_selected": "◆ {platform} ಆಯ್ಕೆ\n\n<i>{platform} ಲಿಂಕ್ ಕಳಿಸಿ:</i>",        "fetching":         "◆ {platform} ನಿಂದ ತರುತ್ತಿದ್ದೇವೆ...",        "auto_detected":    "◆ ಗುರುತಿಸಲಾಗಿದೆ: {platform}",        "download_ready": (            "◆ ಡೌನ್‌ಲೋಡ್ ಸಿದ್ಧ\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>ಲಿಂಕ್ ~20 ನಿಮಿಷ ಮಾನ್ಯ</i>"
        ),
        "btn_download_file": "▸ ಫೈಲ್ ಡೌನ್‌ಲೋಡ್",        "invalid_url":    "◆ ಅಮಾನ್ಯ URL",        "error_generic":  "◆ ದೋಷ ಸಂಭವಿಸಿದೆ\n<code>{err}</code>",        "lang_set":       "◆ ಭಾಷೆ: ಕನ್ನಡ.",        "choose_lang":    "◆ ಭಾಷೆ ಆರಿಸಿ",        "downloads_left": "◇ ಇಂದು {left} ಡೌನ್‌ಲೋಡ್ ಉಳಿದಿವೆ.",        "ad_label":       "◆ — ಜಾಹೀರಾತು —",        "admin_welcome":  "◆ Admin Panel",        "setting_saved":  "◆ ಸೆಟ್ಟಿಂಗ್ ಉಳಿಸಲಾಗಿದೆ.",        "ad_created":     "◆ ಜಾಹೀರಾತು ರಚಿಸಲಾಗಿದೆ.",        "broadcast_done": "◆ {count} ಬಳಕೆದಾರರಿಗೆ ಕಳಿಸಲಾಗಿದೆ.",        "limit_updated":  "◆ ಮಿತಿ: {limit}.",        "not_admin":      "◆ ಪ್ರವೇಶ ನಿರಾಕರಿಸಲಾಗಿದೆ",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "ml": {        "start_caption": (            "◆ സ്വാഗതം, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — യൂണിവേഴ്സൽ മീഡിയ ഡൗൺലോഡർ\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "നിർമ്മിച്ചത്: {team_name}  ·  Dev: {dev_name}\n"
            "<i>സഹായം: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ ഡൗൺലോഡ്",        "btn_help":         "◆ സഹായം",        "btn_premium":      "★ പ്രീമിയം",        "btn_referral":     "◇ റെഫറൽ",        "btn_language":     "◈ ഭാഷ",        "help_text": (            "◆ സഹായം\n"
            "━━━━━━━━━━━━\n"
            "▸ ഡൗൺലോഡ് അമർത്തുക, പ്ലാറ്റ്ഫോം തിരഞ്ഞെടുക്കുക, ലിങ്ക് അയക്കുക\n"
            "▸ അല്ലെങ്കിൽ നേരിട്ട് ലിങ്ക് അയക്കുക\n\n"
            "◆ ദൈനംദിന പരിധി: <code>{limit}</code>\n\n"
            "<i>പിന്തുണ: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev പ്രീമിയം\n"
            "━━━━━━━━━━━━\n"
            "▸ അൺലിമിറ്റഡ് ഡൗൺലോഡ്\n"
            "▸ പരസ്യം ഇല്ല\n"
            "▸ മുൻഗണന പിന്തുണ\n"
            "━━━━━━━━━━━━\n"
            "ബന്ധപ്പെടുക: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ നിങ്ങളുടെ റെഫറൽ ലിങ്ക്\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ പോയിന്റ്: {points}",        "force_join":      "◆ ചാനൽ ആവശ്യം\n\n▸ ചാനലിൽ ചേരുക.\n▸ പിന്നെ /start അമർത്തുക.",        "limit_reached":   "◆ ദൈനംദിന പരിധി കഴിഞ്ഞു\n\n▸ {limit} ഡൗൺലോഡ് ഉപയോഗിച്ചു.",        "banned_msg":      "◆ ആക്സസ് നിരസിച്ചു",        "choose_platform": "◆ പ്ലാറ്റ്ഫോം തിരഞ്ഞെടുക്കുക",        "platform_selected": "◆ {platform} തിരഞ്ഞെടുത്തു\n\n<i>{platform} ലിങ്ക് അയക്കുക:</i>",        "fetching":         "◆ {platform}-ൽ നിന്ന് കൊണ്ടുവരുന്നു...",        "auto_detected":    "◆ തിരിച്ചറിഞ്ഞു: {platform}",        "download_ready": (            "◆ ഡൗൺലോഡ് തയ്യാർ\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>ലിങ്ക് ~20 മിനിറ്റ് സാധുവാണ്</i>"
        ),
        "btn_download_file": "▸ ഫയൽ ഡൗൺലോഡ്",        "invalid_url":    "◆ അസാധുവായ URL",        "error_generic":  "◆ പിശക് സംഭവിച്ചു\n<code>{err}</code>",        "lang_set":       "◆ ഭാഷ: മലയാളം.",        "choose_lang":    "◆ ഭാഷ തിരഞ്ഞെടുക്കുക",        "downloads_left": "◇ ഇന്ന് {left} ഡൗൺലോഡ് ബാക്കി.",        "ad_label":       "◆ — പരസ്യം —",        "admin_welcome":  "◆ Admin Panel",        "setting_saved":  "◆ ക്രമീകരണം സംരക്ഷിച്ചു.",        "ad_created":     "◆ പരസ്യം സൃഷ്ടിച്ചു.",        "broadcast_done": "◆ {count} ഉപയോക്താക്കൾക്ക് അയച്ചു.",        "limit_updated":  "◆ പരിധി: {limit}.",        "not_admin":      "◆ ആക്സസ് നിരസിച്ചു",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "pa": {        "start_caption": (            "◆ ਜੀ ਆਇਆਂ ਨੂੰ, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — ਯੂਨੀਵਰਸਲ ਮੀਡੀਆ ਡਾਊਨਲੋਡਰ\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "ਬਣਾਇਆ: {team_name}  ·  Dev: {dev_name}\n"
            "<i>ਮਦਦ: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ ਡਾਊਨਲੋਡ",        "btn_help":         "◆ ਮਦਦ",        "btn_premium":      "★ ਪ੍ਰੀਮੀਅਮ",        "btn_referral":     "◇ ਰੈਫਰਲ",        "btn_language":     "◈ ਭਾਸ਼ਾ",        "help_text": (            "◆ ਮਦਦ\n"
            "━━━━━━━━━━━━\n"
            "▸ ਡਾਊਨਲੋਡ ਦਬਾਓ, ਪਲੈਟਫਾਰਮ ਚੁਣੋ, ਲਿੰਕ ਭੇਜੋ\n"
            "▸ ਜਾਂ ਸਿੱਧਾ ਲਿੰਕ ਭੇਜੋ\n\n"
            "◆ ਰੋਜ਼ਾਨਾ ਸੀਮਾ: <code>{limit}</code>\n\n"
            "<i>ਸਹਾਇਤਾ: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev ਪ੍ਰੀਮੀਅਮ\n"
            "━━━━━━━━━━━━\n"
            "▸ ਅਸੀਮਿਤ ਡਾਊਨਲੋਡ\n"
            "▸ ਕੋਈ ਇਸ਼ਤਿਹਾਰ ਨਹੀਂ\n"
            "▸ ਤਰਜੀਹੀ ਸਹਾਇਤਾ\n"
            "━━━━━━━━━━━━\n"
            "ਸੰਪਰਕ: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ ਤੁਹਾਡਾ ਰੈਫਰਲ ਲਿੰਕ\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ ਪੁਆਇੰਟ: {points}",        "force_join":      "◆ ਚੈਨਲ ਜ਼ਰੂਰੀ\n\n▸ ਚੈਨਲ ਜੁਆਇਨ ਕਰੋ.\n▸ ਫਿਰ /start ਦਬਾਓ.",        "limit_reached":   "◆ ਰੋਜ਼ਾਨਾ ਸੀਮਾ ਖਤਮ\n\n▸ {limit} ਡਾਊਨਲੋਡ ਵਰਤੇ ਗਏ.",        "banned_msg":      "◆ ਪਹੁੰਚ ਰੱਦ",        "choose_platform": "◆ ਪਲੈਟਫਾਰਮ ਚੁਣੋ",        "platform_selected": "◆ {platform} ਚੁਣਿਆ\n\n<i>{platform} ਲਿੰਕ ਭੇਜੋ:</i>",        "fetching":         "◆ {platform} ਤੋਂ ਲਿਆ ਰਿਹਾ ਹੈ...",        "auto_detected":    "◆ ਪਛਾਣਿਆ: {platform}",        "download_ready": (            "◆ ਡਾਊਨਲੋਡ ਤਿਆਰ\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>ਲਿੰਕ ~20 ਮਿੰਟ ਵੈਧ</i>"
        ),
        "btn_download_file": "▸ ਫਾਈਲ ਡਾਊਨਲੋਡ",        "invalid_url":    "◆ ਗਲਤ URL",        "error_generic":  "◆ ਗੜਬੜੀ ਹੋਈ\n<code>{err}</code>",        "lang_set":       "◆ ਭਾਸ਼ਾ: ਪੰਜਾਬੀ.",        "choose_lang":    "◆ ਭਾਸ਼ਾ ਚੁਣੋ",        "downloads_left": "◇ ਅੱਜ {left} ਡਾਊਨਲੋਡ ਬਾਕੀ.",        "ad_label":       "◆ — ਇਸ਼ਤਿਹਾਰ —",        "admin_welcome":  "◆ Admin Panel",        "setting_saved":  "◆ ਸੈਟਿੰਗ ਸੇਵ.",        "ad_created":     "◆ ਇਸ਼ਤਿਹਾਰ ਬਣਾਇਆ.",        "broadcast_done": "◆ {count} ਯੂਜ਼ਰਾਂ ਨੂੰ ਭੇਜਿਆ.",        "limit_updated":  "◆ ਸੀਮਾ: {limit}.",        "not_admin":      "◆ ਪਹੁੰਚ ਰੱਦ",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "ur": {        "start_caption": (            "◆ خوش آمدید، {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — یونیورسل میڈیا ڈاؤنلوڈر\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "بنایا: {team_name}  ·  Dev: {dev_name}\n"
            "<i>مدد: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ ڈاؤنلوڈ",        "btn_help":         "◆ مدد",        "btn_premium":      "★ پریمیم",        "btn_referral":     "◇ ریفرل",        "btn_language":     "◈ زبان",        "help_text": (            "◆ مدد\n"
            "━━━━━━━━━━━━\n"
            "▸ ڈاؤنلوڈ دبائیں، پلیٹ فارم چنیں، لنک بھیجیں\n"
            "▸ یا براہ راست لنک بھیجیں\n\n"
            "◆ روزانہ حد: <code>{limit}</code>\n\n"
            "<i>سپورٹ: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev پریمیم\n"
            "━━━━━━━━━━━━\n"
            "▸ لامحدود ڈاؤنلوڈ\n"
            "▸ کوئی اشتہار نہیں\n"
            "▸ ترجیحی سپورٹ\n"
            "━━━━━━━━━━━━\n"
            "رابطہ کریں: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ آپ کا ریفرل لنک\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ پوائنٹس: {points}",        "force_join":      "◆ چینل ضروری\n\n▸ چینل جوائن کریں.\n▸ پھر /start دبائیں.",        "limit_reached":   "◆ روزانہ حد ختم\n\n▸ {limit} ڈاؤنلوڈ استعمال ہو گئے.",        "banned_msg":      "◆ رسائی مسترد",        "choose_platform": "◆ پلیٹ فارم چنیں",        "platform_selected": "◆ {platform} منتخب\n\n<i>{platform} لنک بھیجیں:</i>",        "fetching":         "◆ {platform} سے لا رہے ہیں...",        "auto_detected":    "◆ شناخت: {platform}",        "download_ready": (            "◆ ڈاؤنلوڈ تیار\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>لنک ~20 منٹ درست</i>"
        ),
        "btn_download_file": "▸ فائل ڈاؤنلوڈ",        "invalid_url":    "◆ غلط URL",        "error_generic":  "◆ خرابی آئی\n<code>{err}</code>",        "lang_set":       "◆ زبان: اردو.",        "choose_lang":    "◆ زبان چنیں",        "downloads_left": "◇ آج {left} ڈاؤنلوڈ باقی.",        "ad_label":       "◆ — اشتہار —",        "admin_welcome":  "◆ Admin Panel",        "setting_saved":  "◆ سیٹنگ محفوظ.",        "ad_created":     "◆ اشتہار بنایا.",        "broadcast_done": "◆ {count} صارفین کو بھیجا.",        "limit_updated":  "◆ حد: {limit}.",        "not_admin":      "◆ رسائی مسترد",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "de": {        "start_caption": (            "◆ Willkommen, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — Universeller Medien-Downloader\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "Von {team_name}  ·  Dev: {dev_name}\n"
            "<i>Hilfe: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ Herunterladen",        "btn_help":         "◆ Hilfe",        "btn_premium":      "★ Premium",        "btn_referral":     "◇ Empfehlung",        "btn_language":     "◈ Sprache",        "help_text": (            "◆ Hilfe\n"
            "━━━━━━━━━━━━\n"
            "▸ Herunterladen tippen, Plattform wählen, Link senden\n"
            "▸ Oder Link direkt senden\n\n"
            "◆ Tageslimit: <code>{limit}</code>\n\n"
            "<i>Support: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev Premium\n"
            "━━━━━━━━━━━━\n"
            "▸ Unbegrenzte Downloads\n"
            "▸ Werbefrei\n"
            "▸ Prioritäts-Support\n"
            "━━━━━━━━━━━━\n"
            "Kontakt: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ Dein Empfehlungslink\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ Punkte: {points}",        "force_join":      "◆ Kanal erforderlich\n\n▸ Trete dem Kanal bei.\n▸ Dann /start drücken.",        "limit_reached":   "◆ Tageslimit erreicht\n\n▸ {limit} Downloads verbraucht.",        "banned_msg":      "◆ Zugriff verweigert",        "choose_platform": "◆ Plattform wählen",        "platform_selected": "◆ {platform} gewählt\n\n<i>{platform}-Link senden:</i>",        "fetching":         "◆ Lade von {platform}...",        "auto_detected":    "◆ Erkannt: {platform}",        "download_ready": (            "◆ Bereit zum Herunterladen\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>Link ~20 Minuten gültig</i>"
        ),
        "btn_download_file": "▸ Datei herunterladen",        "invalid_url":    "◆ Ungültige URL",        "error_generic":  "◆ Fehler aufgetreten\n<code>{err}</code>",        "lang_set":       "◆ Sprache: Deutsch.",        "choose_lang":    "◆ Sprache wählen",        "downloads_left": "◇ Heute noch {left} Downloads.",        "ad_label":       "◆ — Gesponsert —",        "admin_welcome":  "◆ Admin-Panel",        "setting_saved":  "◆ Einstellung gespeichert.",        "ad_created":     "◆ Anzeige erstellt.",        "broadcast_done": "◆ An {count} Nutzer gesendet.",        "limit_updated":  "◆ Limit: {limit}.",        "not_admin":      "◆ Zugriff verweigert",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "ja": {        "start_caption": (            "◆ ようこそ、{first_name}！\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — ユニバーサルメディアダウンローダー\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "制作: {team_name}  ·  Dev: {dev_name}\n"
            "<i>サポート: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ ダウンロード",        "btn_help":         "◆ ヘルプ",        "btn_premium":      "★ プレミアム",        "btn_referral":     "◇ 紹介",        "btn_language":     "◈ 言語",        "help_text": (            "◆ ヘルプ\n"
            "━━━━━━━━━━━━\n"
            "▸ ダウンロードをタップ、プラットフォームを選択、リンクを送信\n"
            "▸ または直接リンクを送信\n\n"
            "◆ 1日の上限: <code>{limit}</code>\n\n"
            "<i>サポート: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev プレミアム\n"
            "━━━━━━━━━━━━\n"
            "▸ 無制限ダウンロード\n"
            "▸ 広告なし\n"
            "▸ 優先サポート\n"
            "━━━━━━━━━━━━\n"
            "お問い合わせ: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ あなたの紹介リンク\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ ポイント: {points}",        "force_join":      "◆ チャンネル参加が必要\n\n▸ チャンネルに参加してください.\n▸ その後 /start を押してください.",        "limit_reached":   "◆ 本日の上限に達しました\n\n▸ {limit}件のダウンロードを使いました.",        "banned_msg":      "◆ アクセス拒否",        "choose_platform": "◆ プラットフォームを選択",        "platform_selected": "◆ {platform} 選択済み\n\n<i>{platform} のリンクを送信:</i>",        "fetching":         "◆ {platform} から取得中...",        "auto_detected":    "◆ 検出: {platform}",        "download_ready": (            "◆ ダウンロード準備完了\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>リンクは約20分有効</i>"
        ),
        "btn_download_file": "▸ ファイルをダウンロード",        "invalid_url":    "◆ 無効なURL",        "error_generic":  "◆ エラーが発生しました\n<code>{err}</code>",        "lang_set":       "◆ 言語: 日本語.",        "choose_lang":    "◆ 言語を選択",        "downloads_left": "◇ 本日あと{left}件ダウンロード可能.",        "ad_label":       "◆ — 広告 —",        "admin_welcome":  "◆ 管理者パネル",        "setting_saved":  "◆ 設定を保存しました.",        "ad_created":     "◆ 広告を作成しました.",        "broadcast_done": "◆ {count}人に送信しました.",        "limit_updated":  "◆ 上限: {limit}.",        "not_admin":      "◆ アクセス拒否",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "ko": {        "start_caption": (            "◆ 환영합니다, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — 유니버설 미디어 다운로더\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "제작: {team_name}  ·  Dev: {dev_name}\n"
            "<i>지원: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ 다운로드",        "btn_help":         "◆ 도움말",        "btn_premium":      "★ 프리미엄",        "btn_referral":     "◇ 추천",        "btn_language":     "◈ 언어",        "help_text": (            "◆ 도움말\n"
            "━━━━━━━━━━━━\n"
            "▸ 다운로드 탭, 플랫폼 선택, 링크 전송\n"
            "▸ 또는 직접 링크 전송\n\n"
            "◆ 일일 한도: <code>{limit}</code>\n\n"
            "<i>지원: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev 프리미엄\n"
            "━━━━━━━━━━━━\n"
            "▸ 무제한 다운로드\n"
            "▸ 광고 없음\n"
            "▸ 우선 지원\n"
            "━━━━━━━━━━━━\n"
            "문의: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ 추천 링크\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ 포인트: {points}",        "force_join":      "◆ 채널 가입 필요\n\n▸ 채널에 가입하세요.\n▸ 그 다음 /start를 누르세요.",        "limit_reached":   "◆ 일일 한도 도달\n\n▸ {limit}회 다운로드를 사용했습니다.",        "banned_msg":      "◆ 접근 거부",        "choose_platform": "◆ 플랫폼 선택",        "platform_selected": "◆ {platform} 선택됨\n\n<i>{platform} 링크 전송:</i>",        "fetching":         "◆ {platform}에서 가져오는 중...",        "auto_detected":    "◆ 감지됨: {platform}",        "download_ready": (            "◆ 다운로드 준비 완료\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>링크 약 20분 유효</i>"
        ),
        "btn_download_file": "▸ 파일 다운로드",        "invalid_url":    "◆ 잘못된 URL",        "error_generic":  "◆ 오류 발생\n<code>{err}</code>",        "lang_set":       "◆ 언어: 한국어.",        "choose_lang":    "◆ 언어 선택",        "downloads_left": "◇ 오늘 {left}회 다운로드 남음.",        "ad_label":       "◆ — 광고 —",        "admin_welcome":  "◆ 관리자 패널",        "setting_saved":  "◆ 설정 저장됨.",        "ad_created":     "◆ 광고 생성됨.",        "broadcast_done": "◆ {count}명에게 전송됨.",        "limit_updated":  "◆ 한도: {limit}.",        "not_admin":      "◆ 접근 거부",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },

    "zh": {        "start_caption": (            "◆ 欢迎, {first_name}!\n"
            "━━━━━━━━━━━━\n"
            "{bot_name} — 通用媒体下载器\n\n"
            "▸ YouTube  ▸ Instagram  ▸ TikTok\n"
            "▸ Facebook  ▸ Twitter  ▸ Terabox  ▸ Spotify\n\n"
            "━━━━━━━━━━━━\n"
            "作者: {team_name}  ·  Dev: {dev_name}\n"
            "<i>帮助: @MR_ARMAN_08</i>"
        ),
        "btn_download_now": "▸ 下载",        "btn_help":         "◆ 帮助",        "btn_premium":      "★ 高级版",        "btn_referral":     "◇ 推荐",        "btn_language":     "◈ 语言",        "help_text": (            "◆ 使用指南\n"
            "━━━━━━━━━━━━\n"
            "▸ 点击下载，选择平台，发送链接\n"
            "▸ 或直接发送链接\n\n"
            "◆ 每日限制: <code>{limit}</code>\n\n"
            "<i>支持: @MR_ARMAN_08</i>"
        ),
        "premium_text": (            "★ TeamDev 高级版\n"
            "━━━━━━━━━━━━\n"
            "▸ 无限下载\n"
            "▸ 无广告\n"
            "▸ 优先支持\n"
            "━━━━━━━━━━━━\n"
            "联系: @MR_ARMAN_08"
        ),
        "referral_text":   "◇ 你的推荐链接\n━━━━━━━━━━━━\n<code>{ref_link}</code>\n\n◆ 积分: {points}",        "force_join":      "◆ 需要加入频道\n\n▸ 请加入我们的频道.\n▸ 然后按 /start.",        "limit_reached":   "◆ 已达每日限制\n\n▸ 今天 {limit} 次下载已用完.",        "banned_msg":      "◆ 访问被拒绝",        "choose_platform": "◆ 选择平台",        "platform_selected": "◆ 已选 {platform}\n\n<i>发送 {platform} 链接:</i>",        "fetching":         "◆ 正在从 {platform} 获取...",        "auto_detected":    "◆ 已检测: {platform}",        "download_ready": (            "◆ 下载准备就绪\n"
            "━━━━━━━━━━━━\n"
            "▸ {title}\n"
            "{author_line}{quality_line}{duration_line}{size_line}"
            "━━━━━━━━━━━━\n"
            "<i>链接约20分钟有效</i>"
        ),
        "btn_download_file": "▸ 下载文件",        "invalid_url":    "◆ 无效URL",        "error_generic":  "◆ 发生错误\n<code>{err}</code>",        "lang_set":       "◆ 语言: 中文.",        "choose_lang":    "◆ 选择语言",        "downloads_left": "◇ 今天还剩 {left} 次下载.",        "ad_label":       "◆ — 广告 —",        "admin_welcome":  "◆ 管理员面板",        "setting_saved":  "◆ 设置已保存.",        "ad_created":     "◆ 广告已创建.",        "broadcast_done": "◆ 已发送给 {count} 用户.",        "limit_updated":  "◆ 限制: {limit}.",        "not_admin":      "◆ 访问被拒绝",                            "spotify_fetching": "◆ Fetching Spotify track...\n<i>Downloading MP3, please wait.</i>",        "spotify_sending": "◆ Sending audio file...\n<i>This may take a moment.</i>",        "spotify_only_tracks": "◆ Spotify Support\n\n▸ Only individual <b>track</b> links are supported.\n▸ Albums and playlists are not supported yet.",    },
}

SUPPORTED_LANGUAGES = {
    "en": "English",    "hi": "हिंदी",    "bn": "বাংলা",    "ta": "தமிழ்",    "te": "తెలుగు",    "mr": "मराठी",    "gu": "ગુજરાતી",    "kn": "ಕನ್ನಡ",    "ml": "മലയാളം",    "pa": "ਪੰਜਾਬੀ",
    "ar": "العربية",    "ur": "اردو",    "ru": "Русский",    "es": "Español",    "pt": "Português",    "fr": "Français",    "id": "Indonesia",    "tr": "Türkçe",    "de": "Deutsch",    "ja": "日本語",    "ko": "한국어",    "zh": "中文",}


def t(lang: str, key: str, **kwargs) -> str:
    pool = STRINGS.get(lang, STRINGS["en"])
    text = pool.get(key, STRINGS["en"].get(key, key))
    try:
        return text.format(**kwargs)
    except (KeyError, IndexError):
        return text