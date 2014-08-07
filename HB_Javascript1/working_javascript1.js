//Exercise 1: 

var sum = 0;
for (var i=0; i<1000; i++) {
    if(i%3===0 || i%5===0){
        sum += i;
    }
}

console.log(sum);

//Exercise 2

function fibonacci_set(max) {
    if(max>1) {
        var l = [0, 1];
        var current_fib = 1;
        while(current_fib < max) {
            l.push(current_fib);
            current_fib = l[l.length-1] + l[l.length-2];
        }
        return l;
    }
    else {
        return [1, 1];
    }
}

function sum_evens (l) {
    var sum = 0;
    for (i=0; i<l.length; i++) {
        if(l[i]%2=== 0) {
        sum += l[i];
        }
    }
    return sum;
}

console.log(fibonacci_set(4000000));
console.log(sum_evens(fibonacci_set(4000000)));



//Exercise 3

var votesToGoEatCake = [true, true, true, true];
var hackbrightStudents = ["katie", "amy", "jenny", "katie", "kelley", "katie", "amy"];
var classroomIds = [47, 12, 19, 22, 26, 99, 30, 50, 324, 003, 44, 33, 346, 354, 44, 235, 45, 34, 44, 590, 09, 099, 0, 1, 3, 33, 999, 9];
var randomJunkIFound = ["katie", "true", true, 19, "gargoyles", "!", 2 + 3, "2 + 3", 19, "19", 19 === "19", 6, false, false];

function populate_d(l) {
    console.log(l);
    var d = {};
    for(i=0; i<l.length; i++) {
        k = l[i].toString();
        if(k in d) {
            d[k]+= 1;
        }
        else {
          d[k] = 1;
        }
    }
    return d;
}

function check_vals(d) {
    var l = [];
    for(var k in d) {
        if(d[k] > 1) {
            l.push(k);
        }
    }
    return l;
}

console.log(populate_d(votesToGoEatCake));
console.log(check_vals(populate_d(votesToGoEatCake)));

console.log(populate_d(hackbrightStudents));
console.log(check_vals(populate_d(hackbrightStudents)));

console.log(populate_d(classroomIds));
console.log(check_vals(populate_d(classroomIds)));

console.log(populate_d(randomJunkIFound));
console.log(check_vals(populate_d(randomJunkIFound)));

//Exercise 4

var cat = {
    tiredness:50,
    hunger:50,
    loneliness:50,
    happiness:50,
    sleep:function() {
        this.tiredness -= 5;
    },
    feed:function() {
        this.hunger -= 5;
    },
    befriend:function() {
        this.loneliness -= 5;
    },
    pet:function() {
        this.happiness -= 5;
    }

};

function printStatus(arg) {
    console.log("tiredness: " + arg.tiredness + ",");
    console.log("hunger: " + arg.hunger + ",");
    console.log("loneliness: " + arg.loneliness + ",");
    console.log("happiness: " + arg.loneliness);
}

printStatus(cat);
cat.sleep();
printStatus(cat);

//Exercise 5

//can track current book(last book on bookShelf)

var Book = function(title, genre, author, read, readDate) {
    this.title = title || "No title";
    this.genre = genre || "No genre";
    this.author = author || "No author";
    this.read = read || false;
    this.readDate = Date.parse(readDate) || null;
};

var BookList = function(book, bookShelf, readArray, notReadArray) {
    this.book = book;
    this.bookShelf = bookShelf || [];
    this.readArray = readArray || [];
    this.numBooksRead = this.readArray.length || 0;
    this.notReadArray = notReadArray || [];
    this.numBooksNotRead = this.notReadArray.length || 0;
    this.currentBook = this.notReadArray[0] || null;
    this.nextBook = this.notReadArray[1] || null;
    this.lastBookRead = this.readArray[this.readArray.length - 1] || null;

    this.addBook = function(book) {
        //can assume all books go on shelf unread
        this.bookShelf.push(book);
        this.notReadArray.push(book);
        this.currentBook = this.notReadArray[0];
    };

    this.finishCurrentBook = function() {
        this.currentBook.read = true;
        this.currentBook.readDate = Date.now();
        this.readArray.push(this.currentBook);
        this.notReadArray.shift();
        this.currentBook = this.notReadArray[0];

    };

    this.lastBookRead = function(bookShelf) {
        return this.lastBookRead;
    };

    this.nextBookToRead = function(bookShelf) {
        if(this.notReadArray.length){
           return this.nextBook;
        }
        else {
            console.log("No more books to read from the shelf.");
        }
    };
};

var b1 = new Book("Atlas Shrugged", "Fiction", "Ayn Rand", false, null);
var b2 = new Book("Jane Eyre", "Fiction", "Charlotte Bronte", false, null);
var b3 = new Book("Wuthering Heights", "Fiction", "Emily Bronte", false, null);
var b4 = new Book("The Sound and the Fury", "Fiction", "William Faulkner", false, null);
var b5 = new Book("Invisiable Man", "Fiction", "Ralph Ellison", false, null);
var b6 = new Book("Breakfast of Champions", "Fiction", "Kurt Vonnegut", false, null);

var test_list = new BookList(b1);
test_list.addBook(b1);
test_list.addBook(b2);
test_list.addBook(b3);
test_list.addBook(b4);
console.log("****BOOK LIST****");
console.log(test_list.bookShelf);
console.log("\n");

console.log("****CURRENT BOOK****");
test_list.finishCurrentBook();
console.log(test_list.currentBook);

console.log("****NEXT BOOK****");
test_list.nextBookToRead();
console.log(test_list.nextBookToRead());

console.log("*****READ ARRAY****");
console.log(test_list.readArray);
console.log("\n");

console.log("***CURRENT BOOK****");
console.log(test_list.currentBook);

console.log("*****NOT READ ARRAY****");
console.log(test_list.notReadArray);
