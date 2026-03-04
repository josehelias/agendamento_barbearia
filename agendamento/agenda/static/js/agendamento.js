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

            let html = `
                <label for="id_hora">Selecione um horário:</label>
                <select id="id_hora" name="hora" required class="form-select mt-2">
            `;

            data.horarios.forEach(hora => {
                html += `<option value="${hora}">${hora}</option>`;
            });

            html += `</select>`;

            divHorarios.innerHTML = html;

        })
        .catch(() => {
            divHorarios.innerHTML = "Erro ao carregar horários.";
        });
}
// Ouvintes de eventos (Listeners)
selectBarbeiro.addEventListener('change', atualizarHorarios);
inputData.addEventListener('change', atualizarHorarios);

// Executa a função ao carregar, caso o navegador tenha mantido valores nos campos
window.addEventListener('DOMContentLoaded', atualizarHorarios);