const btnEdit = document.querySelectorAll('.edit');
const noId = document.getElementById('noId');
const txtName = document.getElementById('nombre');
const txtDesc = document.getElementById('description');

const tId = document.querySelectorAll('.tId');
const tName = document.querySelectorAll('.tName');
const tDesc = document.querySelectorAll('.tDesc');

const changeAct = document.getElementById('changeAction');
const actionBtn = document.getElementById('nameBtn');
for(let i = 0; i < btnEdit.length; i++) {
    btnEdit[i].addEventListener('click', (e) => {
        noId.value = tId[i].innerHTML;
        txtName.value = tName[i].innerHTML;
        txtDesc.textContent = tDesc[i].innerHTML;
        e.preventDefault();

        changeAct.setAttribute('action', '/updateTask');
        actionBtn.textContent = 'Update task';
    });
}


const btnDelete = document.querySelectorAll('.delete');

for(let i = 0; i < btnDelete.length; i++) {
    btnDelete[i].addEventListener('click', (e) => {
        noId.value = tId[i].innerHTML;
        e.preventDefault();

        changeAct.setAttribute('action', '/deleteTask');
    });
}