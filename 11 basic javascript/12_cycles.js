var students = ["Maria", "Sergio", "Rosa", "Daniel"]
students_copy = [...students]


function greetStudent(student){
    console.log(`Hello there ${student}`)
}

for(var i=0; i<students.length; i++){
    greetStudent(students[i])
}

for (var student of students){
    greetStudent(student)
}


while(students_copy.length){
    greetStudent(students_copy.pop() + " while ")
}