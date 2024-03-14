import sqlite3

# #Open database
conn = sqlite3.connect('test_database.db')

#Create table
conn.execute('''CREATE TABLE users 
		(userId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)''')

conn.execute('''CREATE TABLE products
		(productId INTEGER PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER,
		categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		)''')

conn.execute('''CREATE TABLE kart
		(userId INTEGER,
		productId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')
conn.execute('''CREATE TABLE categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT
		)''')

# last
#1 category is hot coffee
#2 category is cold coffee
#3 category is deserts
#4 category is savoury

product_data=[
    (2, 'Cappucino', 160.0, 'Hot coffee', 'cappuccino.jpg', 2, 1),
(3, 'Desi kulhad coffee', 180.0, 'Hot coffee', 'kulhadcoffee.jpg', 7, 1),
(4, 'Dalgona coffee', 240.0, 'Hot coffee', 'dalgona.jpg', 4, 2),
(5, 'Frappe coffee', 280.0, 'cold coffee', 'frappe.jpg', 2, 2),
(6, 'Hazelnut coffee', 180.0, 'cold coffee', 'hazelnut coffee.jpg', 3, 2),
(7, 'Latte', 160.0, 'Hot coffee', 'latte.jpg', 4, 1),
(8, 'Pasta', 320.0, 'Savoury', 'pasta.jpg', 5, 4),
(9, 'Sandwiches', 300.0, 'Savoury', 'sandwiches.jpg', 1, 4),
(10, 'Vegetable wrap', 320.0, 'Savoury', 'vegetable wrap.jpg', 2, 4),
(11, 'Nachos', 340.0, 'Savoury', 'Nachos.jpg', 3, 4),
(12, 'Fries', 300.0, 'Savoury', 'fries.jpg', 4, 4),
(13, 'Muffin', 140.0, 'Dessert', 'muffin.jpg', 5, 3),
(14, 'Donut', 160.0, 'Dessert', 'donuts.jpeg', 1, 3),
(15, 'croissant', 190.0, 'Dessert', 'croissant.jpg', 8, 3),
(16, 'Pastry', 200.0, 'Dessert', 'pastry1.jpg', 8, 3),
(17, 'oreo shake', 250.0, 'Cold beverage', 'oreo shake.jpg', 8, 2),
(18, 'Americano', 250.0, 'Hot coffee', 'americano.jpg', 8, 1),
(19, 'glace coffee', 250.0, 'cold coffee', 'glace coffee.jpg', 8, 2),
(20, 'espresso', 180.0, 'hot coffee', 'espresso.jpg', 8, 1),
(21, 'Chocolate pastry', 190.0, 'Dessert', 'pastry.jpeg', 8, 3)
]

categories_data=[
    (1, 'hot coffee'),
(2, 'cold coffee'),
(3, 'desserts'),
(4, 'savoury')
]

users_data=[
    (1, '0cc175b9c0f1b6a831c399e269772661', 'abcd@example.com', 'Harsh', 'Shah', 'scaa', 'asa', 'as', 'asc', 'dasd', 'dfas', 'dsa'),
(2, '5e8ff9bf55ba3508199d22e984129be6', 'sample@example.com', 'Sample', 'Name', 'line1', 'line2', 'zipcode', 'abc', 'xyz', 'USA', '1234'),
(3, 'c44a471bd78cc6c2fea32b9fe028d30a', 'virengarg@gmail.com', 'viren', 'ljdlj', 'lkjlj', 'ljlj', 'ljljlj', 'ljlj', 'ljlj', 'ljlj', 'ljlj')
]

conn.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?)", product_data)
conn.executemany("INSERT INTO categories VALUES (?, ?)", categories_data)
conn.executemany("INSERT INTO users VALUES (?, ?,?,?,?,?,?,?,?,?,?,?)", users_data)
conn.commit()
conn.close()

