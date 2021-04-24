const noId = document.getElementById('noId');
const tId = document.querySelectorAll('.tId');
const btnDelete = document.querySelectorAll('.delete');


const changeAct = document.getElementById('changeAction');
for(let i = 0; i < btnDelete.length; i++) {
    btnDelete[i].addEventListener('click', (e) => {
        noId.value = tId[i].innerHTML;
        e.preventDefault();

        changeAct.setAttribute('action', '/deleteTask');
    });
}