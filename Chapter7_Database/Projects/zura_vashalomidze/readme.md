# სამუშაო თასკი
ააწყვეთ Flask-ის აპლიკაცია რომელშიც გაწერილი იქნება SQLalchemy-ს ბაზის მოდელები შემდეგი სტრუქტურით:

მოდელი 1 - Subject
ატრიბუტები:
- id
- title
- students
- teacher

მოდელი 2 - Teacher
- id
- first_name
- last_name
- subject_id (one to one rel. with Subject)

მოდელი 3 - Student
- id
- first_name
- last_name
- subject_id (one to many rel. with Subject)

შექმენით სკრიპტი რომელიც ბაზაში ჩაამატებს  შემდეგ მონაცემებს:
- 2 მასწავლებელი
- 2 საგანი
- 10 სტუდენტი

შექმენით GET მეთოდი რომელიც უკან დააბრუნებს შემდეგ JSONს:

    { subjects : [
    { 'title' : <subject_title>,
      'teacher' : <first_name + last_name>,
      'students' : [<list of students first_name + last_name>]
    }
  ] 
}
