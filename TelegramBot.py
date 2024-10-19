from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
TOKEN = '7029103499:AAGTuXTGfx4pMiDZH_GJPvb1vMMXgP5Z9FI'
current_directory = os.path.dirname(__file__)
image_directory = os.path.join(current_directory , 'image')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['ابزارهای مالی','تامین مالی','سبدگردان'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'صنایع مفتول'],

    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
    await update.message.reply_text(
        f'سلام {update.effective_user.first_name} عزیز \n'
        'به ربات ایساتیس پویا خوش آمدید.\n'
        'می‌توانید جهت اطلاع از فعالیت‌های شرکت‌ها، به کانال‌ شرکت مورد نظرتون بپیوندید و از آخرین اخبار و فعالیت‌ها مطلع شوید. '
        'لطفاً کانال مد نظر خود را از منوی زیر انتخاب کرده و جوین شوید.',
        reply_markup=reply_markup
    )
    

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['ابزارهای مالی','تامین مالی','سبدگردان'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'صنایع مفتول'],

    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)
    await update.message.reply_text(
         'لطفاً شرکت  مد نظر خود را از منوی زیر انتخاب کرده.',
        reply_markup=reply_markup
    )
    


async def show_submenu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    if text=='گروه مالی و سرمایه گذاری ایساتیس پویا' :
        submenu_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['ابزارهای مالی','تامین مالی','سبدگردان'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'صنایع مفتول'],

                           ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        image = os.path.join(image_directory , 'isatispooya.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='گروه مالی ایساتیس پویا\n 🌐 https://isatispooya.com/' , reply_to_message_id=update.message.id) 

# Visa
        
    if text == 'سرمایه گذاری':
        submenu_keyboard = [
            ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
            ['سبدگردانی', 'کارگزاری','ویسا'],
            ['بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
            reply_markup=reply_markup
        )

    elif text == 'کارگزاری':
        # await update.message.reply_text('اینجا لینک سایت رسمی گروه مالی و سرمایه گذاری ایساتیس پویا قرار می‌گیرد.')
        image = os.path.join(image_directory , 'ipb.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='کارگزاری ایساتیس پویا\n 🌐 https://ipb.ir/' , reply_to_message_id=update.message.id) 
 
    elif text == 'ویسا':
        image = os.path.join(image_directory , 'isatisvisa.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='سرمایه گذاری ایساتیس پویا\n 🌐 https://visa.isatispooya.ir/' , reply_to_message_id=update.message.id) 

    elif text == 'سبدگردانی':
        image = os.path.join(image_directory , 'isatispm.png')

        await update.message.reply_photo(photo=open(image,'rb'), caption='سبدگردانی ایساتیس پویا\n 🌐 https://isatispm.ir/' , reply_to_message_id=update.message.id) 

    elif text == 'بازگشت به منوی اصلی':
        await back(update, context)

# Bours

    if text == 'بورس':   
        submenu_keyboard = [
            ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
            ['اوراق','کالا و انرژی'],
            ['بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
            reply_markup=reply_markup
        )
    elif text == 'اوراق':
        image = os.path.join(image_directory , 'ipb.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='اوراق\n 🌐 https://ipb.ir/' , reply_to_message_id=update.message.id) 
    
    elif text == 'کالا و انرژی':
        image = os.path.join(image_directory , 'ipb.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='کالا و انرژی\n 🌐 https://www.ime.co.ir/' , reply_to_message_id=update.message.id) 



# Insurance

    if text == 'بیمه':
        submenu_keyboard = [
            ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
            ['بیمه زندگی','کارگزاری بیمه'],
            ['بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
            reply_markup=reply_markup
        )
    elif text == 'بیمه زندگی':
        image = os.path.join(image_directory , 'insurance.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='بیمه زندگی \n 🌐 https://insurance.isatispooya.com/' , reply_to_message_id=update.message.id) 

    elif text == 'کارگزاری بیمه':
        image = os.path.join(image_directory , 'ipin.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='کارگزاری بیمه\n 🌐 https://ipin.ir/' , reply_to_message_id=update.message.id) 


# Isatispm

    if text == 'سبدگردان':
        submenu_keyboard = [
            ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
            ['سبدگردانی اختصاصی','مشاوره سرمایه گذاری'],
            ['بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
            reply_markup=reply_markup
        )
    elif text == 'سبدگردانی اختصاصی':
        image = os.path.join(image_directory , 'isatispm.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='سبدگردانی ایساتیس پویا\n 🌐 https://isatispm.ir/' , reply_to_message_id=update.message.id) 
    
    elif text == 'مشاوره سرمایه گذاری':
        image = os.path.join(image_directory , 'isatispm.pn')
        await update.message.reply_photo(photo=open(image,'rb'), caption='مشاوره سرمایه گذاری ایساتیس پویا\n 🌐 https://isatispm.ir/' , reply_to_message_id=update.message.id) 



# Sabad

    if text == 'ابزارهای مالی':
        submenu_keyboard = [
            ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
            ['صندوق سرمایه گذاری ترمه','صندوق سرمایه گذاری خاتم','صندوق بازارگردانی'],
            ['صندوق سرمایه‌گذاری مشترک','صندوق سرمایه گذاری خصوصی اکسیر زیست پارسیان'],
            ['بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        await update.message.reply_text(
            'لطفاً یکی از گزینه‌های زیر را انتخاب کنید:',
            reply_markup=reply_markup
        )




# Ipmill

    if text == 'صنایع مفتول':
        submenu_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

                           ]
        
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        image = os.path.join(image_directory , 'isatisvisa.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='صنایع مفتول ایساتیس پویا\n 🌐 https://ipmill.isatispooya.com/' , reply_to_message_id=update.message.id) 

# Atieh

    if text == 'آتیه سازان کویر یزدان':
        submenu_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

                           ]
        
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        image = os.path.join(image_directory , 'isatisvisa.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='آتیه سازان کویر یزدان\n 🌐 https://atieh.isatispooya.com/' , reply_to_message_id=update.message.id) 
# Pardisan

    if text == 'عمرانی سفیران پردیسان':
        submenu_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

                           ]
        
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        image = os.path.join(image_directory , 'isatisvisa.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='عمرانی سفیران پردیسان یزد\n 🌐 https://pardisan.isatispooya.com/' , reply_to_message_id=update.message.id) 

# Isatis-crowd

    if text == 'پلتفرم تامین مالی':
        submenu_keyboard = [
        ['گروه مالی و سرمایه گذاری ایساتیس پویا'],
        ['بیمه', 'بورس', 'سرمایه گذاری'],
        ['سبدگردان', 'ابزارهای مالی', 'صنایع مفتول'],
        ['آتیه سازان کویر یزدان', 'عمرانی سفیران پردیسان', 'پلتفرم تامین مالی'],

                           ]
        
        reply_markup = ReplyKeyboardMarkup(submenu_keyboard, one_time_keyboard=False, resize_keyboard=True)
        image = os.path.join(image_directory , 'isatisvisa.png')
        await update.message.reply_photo(photo=open(image,'rb'), caption='پلتفرم تامین مالی ایساتیس پویا\n 🌐 https://isatiscrowd.ir/' , reply_to_message_id=update.message.id) 

async def goodbye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text(f'{update.effective_user.first_name}عزیز\n ممنون که با ما همراه بودید\nگروه مالی ایساتیس پویا ')



app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stop", goodbye))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, show_submenu))
app.run_polling()
