from src.classes.BookReader import BookReader

if __name__ == '__main__':
    reader = BookReader('test_books')
    books = reader.read()

    pd1 = books.to_df(100)
    pd2 = books.to_df(200)
    pd3 = books.to_df(300)
    pd4 = books.to_df(400)
    pd5 = books.to_df(500)

    pd1.to_pickle('test_data_100.pickle')
    pd2.to_pickle('test_data_200.pickle')
    pd3.to_pickle('test_data_300.pickle')
    pd4.to_pickle('test_data_400.pickle')
    pd5.to_pickle('test_data_500.pickle')
