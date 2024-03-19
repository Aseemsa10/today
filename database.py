from pymongo import MongoClient
from configs import cfg

client = MongoClient(cfg.MONGO_URI)

users = client['main']['users']
groups = client['main']['groups']
points = client['mains']['points']
referral = client['mains']['referral']
languages = client['main']['languages']
pro = client['main']['premium']['users']
languages_collection = client['main']['languages']
pro_gp =  client['main']['premium']['groups']
bin = client['main']['bins']
in_channel = client['main']['users']  # تم تصحيح اسم المجموعة
numbers = client['mains']['numbers']
points_numbers = client['mains']['pointss']
orders = client['mains']['orders']
transfer = client['mains']['transfer']
settings = client['main']['settings']


import datetime



#--------------------------------------------------------------------------------------
#def MyOrders(user_id):
def MyLanguage(user_id, language):
    # ابحث عن المستخدم باستخدام معرف المستخدم
    user = languages.find_one({"user_id": user_id})
    
    # إذا تم العثور على المستخدم، قم بتحديث لغته
    if user:
        languages.update_one({"user_id": user_id}, {"$set": {"Language": language}})
    # إذا لم يتم العثور على المستخدم، قم بإدراج مستخدم جديد مع لغته
    else:
        languages.insert_one({"user_id": user_id, "Language": language})

#################################################################

def language(user_id):
    user = languages.find_one({"user_id": user_id})
    if user:
        mylang = user.get(("Language", None))
        return mylang
    return None

########################################################################################


########################################################################################
def add_transfer(user_id, count, time, to_user, opID):
    timee = time.strftime("%Y-%m-%d %H:%M:%S")

    user = transfer.find_one({"user_id": str(user_id)})
    if user:
        new_count = user.get("user_id", 0)
        transfer.insert_one({"user_id": user_id, "Count": int(count), "id_transfer": opID, "To": str(to_user), "time": timee})
    else:
        transfer.insert_one({"user_id": user_id, "Count": int(count), "id_transfer": opID, "To": str(to_user),  "time": timee})
################################################################################################
def all_transfers():
    return transfer.count_documents({})
################################################################################################
def add_order(user_id, id_order,type, amount, link, time):
    user = orders.find_one({"user_id": str(user_id)})
    time_str = time.strftime("%Y-%m-%d %H:%M:%S")
    if user:
        new_count = user.get("user_id", 0)
        orders.insert_one({"user_id": user_id, "id_order": id_order, "amount": amount, "type": type, "link": link, "time": time_str})
    else:
        orders.insert_one({"user_id": user_id, "id_order": id_order, "amount": amount, "type": type, "link": link, "time": time_str})
################################################################################################
def all_orders():
    return orders.count_documents({})
###########################################################################################3###


def update_join_date(user_id):
    join_date = datetime.datetime.now()
    users.update_one(
        {"user_id": user_id},
        {"$set": {"join_date": join_date}},
        upsert=True
    )
def get_user_info(user_id):
    user = users.find_one({"user_id": user_id})
    if user and "join_date" in user:
        join_date = user["join_date"].strftime("%Y-%m-%d %H:%M:%S")
        return join_date
    return False


def join_user(user_id):
    return in_channel.insert_one({"user_id": str(user_id)})


def all_in_channel():
    return in_channel.count_documents({})  # استخدم count_documents مباشرةً




def already_db(user_id):
        user = users.find_one({"user_id" : str(user_id)})
        if not user:
            return False
        return True

def add_user(user_id):
    in_db = already_db(user_id)
    if in_db:
        return
    return users.insert_one({"user_id": str(user_id)}) 

def remove_user(user_id):
    in_db = already_db(user_id)
    if not in_db:
        return 
    return users.delete_one({"user_id": str(user_id)})

def add_points(user_id, addpoints):
    user = points.find_one({"user_id": str(user_id)})
    if user:
        new_points = user.get("points", 0) + addpoints
        points.update_one({"user_id": str(user_id)}, {"$set": {"points": new_points}})
    else:
        points.insert_one({"user_id": str(user_id), "points": addpoints})


def deduct_points(user_id, points_to_deduct):
    user = points.find_one({"user_id": str(user_id)})
    if user:
        current_points = user.get("points", 0)
        new_points = max(0, current_points - points_to_deduct)  # التأكد من عدم السماح بأن يكون الرصيد أقل من الصفر
        points.update_one(
            {"user_id": str(user_id)},
            {"$set": {"points": new_points}}
        )
    else:
        pass  # يمكنك التعامل مع هذه الحالة حسب متطلبات تطبيقك، مثلاً رمي استثناء أو إرسال رسالة تنبيهية

################################################################
def display__transfer(user_id):
    user_transfer = transfer.find({"user_id": user_id})
    all_transfers = []
    for transferr in user_transfer:
        transfer_list = []
        transfer_list.append(f"id_transfer: `{transferr['id_transfer']}`")
        transfer_list.append(f"to: `{transferr['To']}`")
        transfer_list.append(f"count: {transferr['Count']}")
        transfer_list.append(f"Time: {transferr['time']}")
        transfer_list.append("---------------------------")
        all_transfers.append('name'.join(transfer_list))
    return all_transfers





def display_orders(user_id):
    user_orders = orders.find({"user_id": user_id})
    all_orders = []
    for order in user_orders:
        orders_list = []
        orders_list.append(f"Order ID: `{order['id_order']}`")
        orders_list.append(f"Amount: {order['amount']}")
        orders_list.append(f"Type: **{order['type']}**")
        orders_list.append(f"Link: {order['link']}")
        orders_list.append(f"Time: {order['time']}")
        orders_list.append("-----------------------------")
        all_orders.append('name'.join(orders_list))
    return all_orders



#def display_orders(user_id):
#    user_orders = orders.find({"user_id": user_id})
#    all_orders = []
#    for order in user_orders:
#        orders_list = []
#        orders_list.append(f"Order ID: {order['id_order']}")
#        orders_list.append(f"Amount: {order['amount']}")
#        orders_list.append(f"Type: {order['type']}")
#        orders_list.append(f"Link: {order['link']}")
#        orders_list.append(f"Time: {order['time']}")
#        orders_list.append("-----------------------------")
#        all_orders.append(" ".join(orders_list))
#    return all_orders

def get_points(user_id):
    user = points.find_one({"user_id": str(user_id)})
    if user:
        return user.get("points", 0)  # إذا وجد المستخدم، استرجع عدد النقاط، وإذا لم يجده، استرجع صفر
    else:
        return 0  # إذا لم يجد المستخدم، استرجع صفر

def increment_referral_count(referral_id):
    user = referral.find_one({"user_id": str(referral_id)})
    if user:
        new_count = user.get("referral_count", 0) + 1
        referral.update_one({"user_id": str(referral_id)}, {"$set": {"referral_count": new_count}})
    else:
        referral.insert_one({"user_id": str(referral_id), "referral_count": 1})

def get_count(user_id):
    user = referral.find_one({"user_id": str(user_id)})
    if user:
        return user.get("referral_count", 0)  # إذا وجد المستخدم، استرجع عدد النقاط، وإذا لم يجده، استرجع صفر
    else:
        return 0  # إذا لم يجد المستخدم، استرجع صفر

def add_points_numbers(user_id, points):
    user = points_numbers.find_one({"user_id": str(user_id)})
    if user:
        new_points = user.get("points_num", 0) + points
        points_numbers.update_one({"user_id": str(user_id)}, {"$set": {"points_num": new_points}})
    else:
        points_numbers.insert_one({"user_id": str(user_id), "points_num": points})

def add_number(user_id):
    user = numbers.find_one({"user_id": str(user_id)})
    if user:
        new_add = user.get("numbers", 0) + 1
        numbers.update_one({"user_id": str(user_id)}, {"$set": {"numbers": new_add}})
    else:
        numbers.insert_one({"user_id": str(user_id), "numbers": 1})

def get_points_num(user_id):
    user = points_numbers.find_one({"user_id": str(user_id)})
    if user:
        return user.get("points_num", 0)
    else:
        return 0
    
def get_numbers(user_id):
    user = numbers.find_one({"user_id": str(user_id)})
    if user:
        return user.get("numbers", 0)
    else:
        return 0


def all_pro():
    user = pro.find({})
    uss = len(list(user))
    return uss



def add_pro(user_id):
     in_db = already_pro(user_id)
     if in_db:
        return
     return pro.insert_one({"user_id": str(user_id)})

def del_pro(user_id):
    in_db = already_pro(user_id)
    if not in_db:
        return
    return pro.delete_one({"user_id": str(user_id)})


def all_users():
    user = users.find({})
    usrs = len(list(user))
    return usrs

def all_groups():
    group = groups.find({})
    grps = len(list(group))
    return grps

def already_pro(user_id):
    user = pro.find_one({"user_id" : str(user_id)})
    if not user:
        return False
    return True


