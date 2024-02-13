
function generateTable() {  
    const rows = document.getElementById('rows').value;  
    const cols = document.getElementById('cols').value;  
    let table = '<table id=tableclear>';  

    // Header row with criteria names
    table += '<tr>';
    for (let j = 0; j < cols; j++) {  
        table += `<th><input type="text" placeholder="Criteria Name" id="name_${j}"></th>`;  
    }
    table += '</tr>';

    table += '<tr>';
    for (let k = 0; k < cols; k++) {
        table += `<th><select name="criteriaTypes" required id="type_${k}">`;
        table += '<option value="" disabled selected hidden>Criteria Type</option>';
        table += '<option value="NonBeneficial">Non-Beneficial</option>';
        table += '<option value="Beneficial">Beneficial</option>';
        table += '</select></th>';
    }
    table += '</tr>';



    // Rows with input fields
    for (let i = 0; i < rows; i++) {  
        table += '<tr>';  
        for (let j = 0; j < cols; j++) {  
            table += `<td><input type="number" id="value_${i}_${j}" placeholder="Value"></td>`;  
        }  
        table += '</tr>';  
    }  


    table += '</table>';  
    const tableContainer = document.getElementById('table-container');  
    tableContainer.innerHTML = table;
    
    
}

function submitFormData() {
    const rows = document.getElementById('rows').value;
    const cols = document.getElementById('cols').value;

    // Collect table data
    const tableData = [];
    const tableData1 = [];
    for (let i = 0; i < rows; i++) {
        const rowData = [];
        for (let j = 0; j < cols; j++) {
            const cellValue = document.getElementById(`value_${i}_${j}`).value;
            rowData.push(cellValue);
        }
        tableData.push(rowData);
    }
    
    for (let k = 0; k < cols; k++) {
        const criteriaName = document.getElementById(`name_${k}`).value;
        const criteriaType = document.getElementById(`type_${k}`).value;
        tableData1.push(criteriaName);
        tableData1.push(criteriaType);
    }

    $.ajax({
        type: 'POST',
        url: '/',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ tableData, tableData1 }),
        success: function (data) {
            $('#results-container').html('The best choice of your alternatives is: ' + data.best_alternative + ' ranks 1st with a performance score of ' + data.best_perf_score);
        },
        
        error: function (error) {
            console.error('Error:', error);
        }
    });
}

