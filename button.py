from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

## Bot in Start
ButtonsStart = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("- خدمات البوت Ⓜ️", callback_data="service")
        ],
        [
            InlineKeyboardButton("- معلوماتك 🚦", callback_data="info"),
            InlineKeyboardButton("- شحن الرصيد 💰", callback_data="addfounds")
        ],
        [
            InlineKeyboardButton("- طلباتك 📜", callback_data="myorders"),
            InlineKeyboardButton("- تحويلاتك 📉", callback_data="mytransfer")
        ],
        [
            InlineKeyboardButton("- تحويل رصيد 🔃", callback_data="balance_transfer"),
            InlineKeyboardButton("- شروط الاستخدام 🚧", callback_data="DD")
        ]
    ]
)

A = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ دخول البوت💁‍♂️", url="https://t.me/hsiehrbot?start=start")
                    ]
                ]
            )
keycek = InlineKeyboardMarkup( 
            [ 
                [ 
                    InlineKeyboardButton("تحقق من الاشتراك ⚠️", "chk") 
                ] 
            ] 
        ) 

## Bot in Service
service = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("- رشق أعضاء 👥", callback_data="JoinM")
        ],
        [
            InlineKeyboardButton("- رشق مشاهدات 👁️", callback_data="GetView"),
            InlineKeyboardButton("- تصويت أستفتاء 📉", callback_data="GetPoll")
        ],
        [
            InlineKeyboardButton("- تصويت لايكات عادي 👍", callback_data="GetVoto"),
            InlineKeyboardButton("- تصويت لايكات اجباري ❤️", callback_data="GetVotoPro")
        ],
        [
            InlineKeyboardButton("- تفاعلات 🔥", callback_data="GetR")
        ],
        [
            InlineKeyboardButton("- ألغاء ورجوع 🔙", callback_data="Back")
        ]
    ]
)


back1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("- رجوع 🔙", callback_data="Back1")
        ]
    ]
)
back = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("- رجوع 🔙", callback_data="Back")
        ]
    ]
)

bt_cancel = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("- الغاء العملية", callback_data="cancel")
        ]
    ]
)
menu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⏹️ القائمة الرئيسية", callback_data="Back")
        ]
    ]
)

PriceA = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Finish the order! 🪧", callback_data="PriceDone")
        ],
        [
            InlineKeyboardButton("🔙 Back", callback_data="Back")
        ]
    ]
)

AddFound = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("- دعوة الاصدقاء 👤", callback_data="get_friends"),
            InlineKeyboardButton("- تسليم حسابات 💳", callback_data="send_numbers")
        ],
        [
            InlineKeyboardButton("- شراء النقاط 💰", callback_data="pay")
        ],
        [
            InlineKeyboardButton("🔙 Back", callback_data="Back")
        ]
    ]
)

back_pay = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔙 Back", callback_data="Back_pay")
        ]
    ]
)