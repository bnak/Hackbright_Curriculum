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
    for(k in d) {
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
Array.prototype.diff = function(a) {
    return this.filter(function(i) {return a.indexOf(i) < 0;});
};

var Book = function(title, genre, author, read, read_date) {
    this.title = title || "No title";
    this.genre = genre || "No genre";
    this.author = author || "No author";
    this.read = read || false;
    this.read_date = Date.parse(read_date) || "";
};

var BookList = function(book, bookShelf, readBooks) {
    this.book = book;
    this.bookShelf = bookShelf || [];
    this.lastBookRead = this.bookShelf[this.bookShelf.length - 1] || false;
    this.readBooks = readBooks || [];
    this.notReadBooks = this.bookShelf.diff(this.readBooks) || [];

    this.addBook = function(book, bookShelf){
        if (!(this.book in this.bookShelf)){
            this.bookShelf.push(this.book);
            this.notReadBooks.push(this.book);

        }
    };

    this.finishCurrentBook = function(book){
        this.book.read = true;
        this.book.read_date = Date.now();
    };

    this.booksRead = function(bookShelf) {
        var readBooks = [];
        for(i=0; i<this.bookShelf.length; i++){
            if(this.bookShelf[i].read){
                readBooks.push(this.bookShelf[i]);
            }
        }
        this.readBooks = readBooks;
        return this.readBooks;
    };

    this.lastBookRead = function(bookShelf){
        return this.lastBookRead;
   };

   this.booksNotRead = function(bookShelf){
        return this.notReadBooks;
   };

    //return this.bookShelf;

};


console.log(bookShelf);
var b1 = new Book("Atlas Shrugged", "Fiction", "Ayn Rand", false);
var b2 = new Book("ABC", "Fiction", "Author", false);
console.log(b1);

var test_list = new BookList(b1);
test_list.addBook(b1);
test_list.addBook(b2);

console.log(test_list);
console.log("\n");
console.log("\n");

console.log("\n");
console.log("\n");

console.log(test_list);
console.log("\n");
console.log("\n");

// test_list.finishCurrentBook(b1);
console.log(b1);

console.log(test_list);
console.log("\n");
console.log("\n");

test_list.booksRead();
console.log(test_list.booksRead());
console.log(test_list);
console.log("\n");

test_list.lastBookRead();
console.log(test_list.lastBookRead());

test_list.booksNotRead();
console.log(test_list.booksNotRead());

