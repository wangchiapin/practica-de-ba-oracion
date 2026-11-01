# 積木組句的手寫資料（人物／物品／地點的西英文、哪些物品能放哪裡）。
# 中文詞與讀音不在這裡寫：由 make_blocks.py 從遊戲現有的「放置」句子取出（讀音照 GoodTeacher）。
# 圖片由遊戲裡的 sceneP(物品, 地點, 人物) 畫出；這裡只決定「哪些組合合理」。

WHO = {   # 鍵: (西文主詞, 英文主詞)；我 = 西文不寫主詞、動詞用第一人稱
    'me': ('', 'I'), 'he': ('Él', 'He'), 'she': ('Ella', 'She'),
    'mom': ('Mamá', 'Mom'), 'dad': ('Papá', 'Dad'),
    'tchm': ('El maestro', 'The teacher'), 'tchf': ('La maestra', 'The teacher'),
    'bro': ('Mi hermano mayor', 'My older brother'), 'sis': ('Mi hermana mayor', 'My older sister'),
    'lbro': ('Mi hermano menor', 'My younger brother'), 'lsis': ('Mi hermana menor', 'My younger sister'),
    'gma': ('La abuela', 'Grandma'), 'gpa': ('El abuelo', 'Grandpa'),
    'ming': ('Xiaoming', 'Xiaoming'), 'mei': ('Xiaomei', 'Xiaomei'),
}
WHO_ORDER = ['me', 'he', 'she', 'mom', 'dad', 'tchm', 'tchf', 'bro', 'sis', 'lbro', 'lsis', 'gma', 'gpa', 'ming', 'mei']

# 動詞：鍵 -> (中文詞, 西文第三人稱, 西文第一人稱, 英文)
VERBS = {
    'put': ('放在', 'puso', 'puse', 'put'),
    'in': ('放進', 'metió', 'metí', 'put'),
    'throw': ('丟進', 'tiró', 'tiré', 'threw'),
    'hang': ('掛在', 'colgó', 'colgué', 'hung'),
    'stick': ('貼在', 'pegó', 'pegué', 'stuck'),
    'park': ('停在', 'estacionó', 'estacioné', 'parked'),
    'insert': ('插進', 'metió', 'metí', 'put'),
    'poke': ('插在', 'clavó', 'clavé', 'stuck'),
}

# 地點：鍵 -> (西文, 英文)；門（door）看動詞不同，見 DOOR
PL = {
    'table': ('sobre la mesa', 'on the table'), 'desk': ('sobre el escritorio', 'on the desk'),
    'counter': ('sobre la barra de la cocina', 'on the kitchen counter'), 'shelf': ('en el estante', 'on the shelf'),
    'cabinet': ('sobre el mueble', 'on the cabinet'), 'floor': ('en el piso', 'on the floor'),
    'sill': ('en el alféizar de la ventana', 'on the windowsill'), 'bed': ('sobre la cama', 'on the bed'),
    'sofa': ('en el sofá', 'on the sofa'), 'under': ('debajo de la mesa', 'under the table'),
    'besidechair': ('al lado de la silla', 'next to the chair'), 'besidedoor': ('al lado de la puerta', 'next to the door'),
    'porch': ('en la entrada', 'at the entrance'),
    'fridge': ('en el refrigerador', 'in the fridge'), 'drawer': ('en el cajón', 'in the drawer'),
    'box': ('en la caja', 'in the box'), 'bag': ('en la bolsa', 'in the bag'), 'basket': ('en la canasta', 'in the basket'),
    'suitcase': ('en la maleta', 'in the suitcase'), 'wardrobe': ('en el clóset', 'in the closet'),
    'shoecab': ('en el zapatero', 'in the shoe cabinet'), 'trash': ('al bote de basura', 'in the trash can'),
    'pot': ('en la olla', 'in the pot'), 'trunk': ('en la cajuela del carro', 'in the trunk of the car'),
    'vase': ('en el florero', 'in the vase'), 'penholder': ('en el portalápices', 'in the pen holder'),
    'flowerpot': ('en la maceta', 'in the flower pot'),
    'rack': ('en el perchero', 'on the coat rack'), 'wall': ('en la pared', 'on the wall'),
}
PL_ORDER = ['table', 'desk', 'counter', 'shelf', 'cabinet', 'floor', 'sill', 'bed', 'sofa', 'under', 'besidechair', 'besidedoor', 'porch',
            'fridge', 'drawer', 'box', 'bag', 'basket', 'suitcase', 'wardrobe', 'shoecab', 'trash', 'pot', 'trunk', 'vase', 'penholder', 'flowerpot',
            'rack', 'door', 'wall']
# 門：掛（門後面）／貼（門上）
DOOR = {'hang': ('detrás de la puerta', 'on the back of the door', '門後面'), 'stick': ('en la puerta', 'on the door', '門上')}
STICK = {('poster', 'wall'), ('paper', 'wall'), ('map', 'wall'), ('poster', 'door'), ('paper', 'door'), ('photo', 'door'), ('map', 'door')}
# 動詞要跟地點種類配：垃圾桶＝丟進、筆筒＝插進、花盆＝插在、其他容器＝放進；牆／門／衣架＝掛在（貼的見 STICK）；車＝停在
SPECIAL_IN = {'trash': 'throw', 'penholder': 'insert', 'flowerpot': 'poke'}
IN_PLACES = {'fridge', 'drawer', 'box', 'bag', 'basket', 'suitcase', 'wardrobe', 'shoecab', 'trash', 'pot', 'trunk', 'vase', 'penholder', 'flowerpot'}
HANG_PLACES = {'rack', 'door', 'wall'}
VEHICLES = {'bike', 'moto'}

# 物品：鍵 -> (西文, 英文, [能放的地點])
OB = {
    'pen': ('el lápiz', 'the pencil', 'desk table shelf drawer bag box'),
    'cup': ('la taza', 'the cup', 'table desk counter shelf cabinet'),
    'apple': ('la manzana', 'the apple', 'table counter fridge bag basket'),
    'phone': ('el celular', 'the phone', 'desk table sofa bed shelf drawer bag'),
    'book': ('el libro', 'the book', 'table desk shelf bed sofa drawer box bag suitcase'),
    'bottle': ('la botella de agua', 'the water bottle', 'table desk counter cabinet bag fridge'),
    'ball': ('la pelota', 'the ball', 'floor under shelf box bag sofa'),
    'plant': ('la planta', 'the plant', 'floor sill table desk shelf'),
    'glasses': ('los lentes', 'the glasses', 'table desk sofa bed shelf drawer bag'),
    'wallet': ('la cartera', 'the wallet', 'desk table sofa drawer bag suitcase'),
    'pillow': ('la almohada', 'the pillow', 'bed sofa'),
    'cake': ('el pastel', 'the cake', 'table counter fridge box'),
    'bread': ('el pan', 'the bread', 'table counter bag basket box fridge'),
    'milk': ('la leche', 'the milk', 'table counter fridge bag basket'),
    'laptop': ('la computadora', 'the laptop', 'desk table sofa bed bag suitcase'),
    'notebook': ('el cuaderno', 'the notebook', 'desk table shelf drawer bag box'),
    'backpack': ('la mochila', 'the backpack', 'floor table sofa bed under besidechair besidedoor rack door'),
    'hat': ('el gorro', 'the hat', 'table desk sofa bed shelf wardrobe rack door bag suitcase'),
    'egg': ('el huevo', 'the egg', 'table counter fridge pot basket'),
    'flowers': ('las flores', 'the flowers', 'table desk counter shelf cabinet vase'),
    'scissors': ('las tijeras', 'the scissors', 'desk table drawer bag box'),
    'bowl': ('el tazón', 'the bowl', 'table counter shelf cabinet'),
    'plate': ('el plato', 'the plate', 'table counter shelf cabinet'),
    'chopsticks': ('los palillos', 'the chopsticks', 'table counter drawer'),
    'toy': ('el osito de peluche', 'the teddy bear', 'floor shelf bed sofa box bag basket'),
    'bag': ('la bolsa', 'the bag', 'table desk sofa bed floor under besidechair besidedoor rack door shelf'),
    'umbrella': ('el paraguas', 'the umbrella', 'besidedoor porch rack door floor bag'),
    'shoes': ('los zapatos', 'the shoes', 'porch besidedoor floor under shoecab suitcase bag'),
    'bike': ('la bicicleta', 'the bike', 'porch besidedoor'),
    'moto': ('la moto', 'the scooter', 'porch besidedoor'),
    'juice': ('el jugo', 'the juice', 'table desk counter fridge bag basket'),
    'sock': ('los calcetines', 'the socks', 'drawer bed bag basket suitcase wardrobe'),
    'cookie': ('las galletas', 'the cookies', 'table counter box bag basket'),
    'orange': ('la mandarina', 'the tangerine', 'table counter fridge bag basket'),
    'banana': ('el plátano', 'the banana', 'table counter fridge bag basket'),
    'towel': ('la toalla', 'the towel', 'rack door bed sofa basket drawer bag suitcase'),
    'shirt': ('la ropa', 'the clothes', 'bed sofa rack door wardrobe suitcase basket drawer'),
    'coat': ('el abrigo', 'the coat', 'bed sofa rack door wardrobe suitcase'),
    'paper': ('el papel', 'the paper', 'desk table floor drawer box trash wall door bag'),
    'tissue': ('los pañuelos desechables', 'the tissues', 'table desk drawer trash'),
    'trashbag': ('la bolsa de basura', 'the trash bag', 'besidedoor porch floor trash'),
    'veg': ('las verduras', 'the vegetables', 'table counter fridge pot basket bag'),
    'luggage': ('el equipaje', 'the luggage', 'besidedoor porch floor trunk'),
    'key': ('la llave', 'the key', 'desk table drawer bag box rack door'),
    'clock': ('el reloj de pared', 'the clock', 'wall shelf desk table cabinet'),
    'picture': ('el cuadro', 'the painting', 'wall shelf cabinet floor table'),
    'photo': ('la foto', 'the photo', 'wall door desk table shelf cabinet drawer'),
    'calendar': ('el calendario', 'the calendar', 'wall desk table shelf drawer'),
    'poster': ('el póster', 'the poster', 'wall door floor desk table'),
    'map': ('el mapa', 'the map', 'wall door desk table shelf drawer bag'),
    'cap': ('la gorra', 'the cap', 'table desk sofa bed shelf rack door bag'),
    'mask': ('la mascarilla', 'the mask', 'table desk drawer bag counter'),
    'scarf': ('la bufanda', 'the scarf', 'sofa bed rack door drawer bag suitcase wardrobe basket'),
    'gloves': ('los guantes', 'the gloves', 'table desk drawer bag sofa wardrobe'),
    'watch': ('el reloj de pulsera', 'the watch', 'desk table drawer bag cabinet'),
    'penup': ('el bolígrafo', 'the pen', 'desk table drawer bag penholder'),
    'flag': ('la bandera', 'the flag', 'desk table flowerpot floor shelf'),
}
OB_ORDER = list(OB.keys())
