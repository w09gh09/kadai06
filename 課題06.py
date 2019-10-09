public class Main {
public static void main(String[] args) {
        BookShelf bookShelf = new BookShelf(4);

        bookShelf.appendBook(new Book("GAME1"));
        bookShelf.appendBook(new Book("GAME2"));
        bookShelf.appendBook(new Book("GAME3"));
        bookShelf.appendBook(new Book("GAME4"));

        Iterator iterator = bookShelf.iterator();
        while(iterator.hasNext()) {
            Book book = (Book)iterator.next();
            System.out.println(book.getName());
        }
    }
}
