class Account {
    constructor(name, document){
        this.id;
        this.name = name;
        this.document = document;
        this.email;
        this.password;
    }

    printdata(self){
        console.log('Name: ', this.name);
        console.log('Document: ', this.document);
    }
}