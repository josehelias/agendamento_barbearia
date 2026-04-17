// Seletores dos elementos
const selectBarbeiro = document.querySelector('#barbeiro-select');
const inputData = document.querySelector('#id_data');
const divHorarios = document.querySelector('#grid-horarios');

function atualizarHorarios() {
    const barbeiroId = selectBarbeiro.value;
    const data = inputData.value;

    if (!barbeiroId || !data) {
        divHorarios.innerHTML = "Selecione um barbeiro e uma data para ver os horários disponíveis.";
        return;
    }

    divHorarios.innerHTML = "Carregando horários...";

    fetch(`/buscar-horarios/?barbeiro_id=${barbeiroId}&data=${data}`)
        .then(response => response.json())
        .then(data => {
            divHorarios.innerHTML = "";

            if (data.horarios.length === 0) {
                divHorarios.innerHTML = "Nenhum horário disponível para esta data.";
                return;
            }

            let html = ``;

            data.horarios.forEach(hora => {
                html += `<div class="col-4 col-md-3 col-lg-2 mb-3">
                <button type="button" class="btn btn-outline-warning w-100 btn-horario" data-horario="${hora}">
                    ${hora}
                </button></div>`;
            });

            divHorarios.innerHTML = html;

        })
        .catch(() => {
            divHorarios.innerHTML = "Erro ao carregar horários.";
        });
}

function selecionarHorario(event) {
    
}

document.addEventListener("click", function(e){

    if(e.target.classList.contains("btn-horario")){

        document.querySelectorAll(".btn-horario")
        .forEach(btn => btn.classList.remove("active"))

        e.target.classList.add("active")

        document.getElementById("horario-selecionado").value =
        e.target.dataset.horario
    }

})


// Ouvintes de eventos (Listeners)
selectBarbeiro.addEventListener('change', atualizarHorarios);
inputData.addEventListener('change', atualizarHorarios);

// Executa a função ao carregar, caso o navegador tenha mantido valores nos campos
window.addEventListener('DOMContentLoaded', atualizarHorarios);