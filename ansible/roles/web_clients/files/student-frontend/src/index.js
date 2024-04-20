const studentTableBody = document.querySelector('.student-table-body');
const studentQuery = document.querySelector('#student-query');

async function getStudentList(query = ''){
    const response = await fetch(`http://192.168.144.120:8002/api/students/?query=${query}`);
    const students = await response.json();
    console.log(students);
    const htmls = students.reduce((result, student, index) => {
        return `${result}\n
        <tr>
            <th scope="row">${index + 1}</th>
            <td>${student.full_name}</td>
            <td>${student.username}</td>
            <td>${student.gender}</td>
            <td>${student.birthday}</td>
        </tr>
        `
    }, '')
    studentTableBody.innerHTML = htmls;
}


getStudentList();

function handleSearchStudent(){
    const query = studentQuery.value;
    getStudentList(query);
}

