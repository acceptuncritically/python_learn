#完成 图书与书架
class Book:
    def __init__(self, title, author, price,stock=1):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    def __str__(self):
        return f'《{self.title}》-{self.author}-￥{self.price}'
    def describe(self):  # 补上缺失的方法
        return f"《{self.title}》- {self.author} - ￥{self.price}"
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return self.price < other.price
class BookShelf:
    def __init__(self):
        self.books = []
    def add(self,add_book):
        for book in self.books:
            if add_book == book:
                book.stock+=1
                return True
        self.books.append(add_book)
        return True
    def remove(self,remove_title):
        for book in self.books:
            if book.title == remove_title:
                self.books.remove(book)
                print("删除成功")
                return True
        return False
    def find(self,find_title):
        for book in self.books:
            if book.title == find_title:
                return book
        else:
            return None
    def sorted_books(self):
        return sorted(self.books, key=lambda book: book.price)
    def total_value(self):
        return sum(book.price*book.stock for book in self.books)
def main(self):
    shelf = BookShelf()
    while True:
        choice=int(input("1~6"))
        match choice:
            case 1:
                title = input("请输入书名：")
                author = input("请输入作者：")
                try:
                    price = float(input("请输入价格："))
                except ValueError:
                    print("价格输入错误，请输入数字！")
                    continue
                    # 组装成 Book 对象，传给 add
                new_book = Book(title, author, price, 1)
                shelf.add(new_book)
            case 2:
                title = input("请输入要删除的书名：")
                shelf.remove(title)
            case 3:
                title = input("请输入要查找的书名：")
                book = shelf.find(title)
                if book:
                    print(f"找到书籍：{book.describe()}，库存：{book.stock}")
                else:
                    print("未找到该书。")
            case 4:
                print("\n--- 按价格升序的书单 ---")
                sorted_list = shelf.sorted_books()
                if not sorted_list:
                    print("书架为空。")
                for b in sorted_list:
                    print(b.describe(), "库存:", b.stock)
            case 5:
                print(f"当前书架总价值：￥{shelf.total_value()}")
            case _:
                break

if __name__=="__main__":
    main()