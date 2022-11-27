document.addEventListener("DOMContentLoaded", function(event){

    const formContainerEl = document.querySelector("#form-container");
    const providerNameEl = document.querySelector("#provider-name");
    const cardFormTitleEl = document.querySelector("#card-form-title");
    const formEl = document.querySelector("#form");


    // Display form
    document.getElementById("btn-add-new").onclick = function(event){
        formContainerEl.style.display = "block";
        cardFormTitleEl.textContent = "Add New Provider";
        providerNameEl.textContent = "";
        formEl.setAttribute("data-method-type", "POST");
        formEl.setAttribute("data-endpoint", "/provider");
    }

    // Cancel or hide form
    document.getElementById("btn-cance-form").onclick = function(event){
        formContainerEl.style.display = "none";
    }

    formEl.onsubmit = saveDataToDatabase;

    
    loadTable();


})

const saveDataToDatabase = (event) =>{
    event.preventDefault();

    const formEl = document.querySelector("#form");
    const errorContainerEl = document.querySelector("#error-container");
    const errorContentEl = document.querySelector("#error-content");
    const methodType = formEl.getAttribute("data-method-type");// POST or PUT
    const endpoint = formEl.getAttribute("data-endpoint");
    const providerName = document.querySelector("#provider-name").value;
    const btnSaveData = document.querySelector("#btn-save-data");


    // reset error 
    errorContainerEl.style.display = "none";
    errorContentEl.textContent = "";


    // Activate loading
    const loading = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> saving...';
    btnSaveData.innerHTML = loading;
    btnSaveData.disabled = true;

    fetch(endpoint, {
        method:methodType,
        body: JSON.stringify({name: providerName}),
        headers: {"Content-Type": "application/json"}
    }).then(function(response){
        if (response.status === 201 || response.status === 200){
            // Reload the current page
            // to reflect new changes
            window.location.href = "/provider-list";

        }else{


            // set error 
            errorContainerEl.style.display = "block";
            errorContentEl.textContent = "Something went wrong, whilst saving the data!";

            // deactivate loading
            btnSaveData.innerHTML = "Save";
            btnSaveData.disabled = false;

        }

    }).catch(function(err){

        // set error 
        errorContainerEl.style.display = "block";
        errorContentEl.textContent = "Something went wrong, check your network!";

        // deactivate loading
        btnSaveData.innerHTML = "Save";
        btnSaveData.disabled = false;

    })
    

}


const loadTable = () => {
   
    const tableSpinnerEl = document.getElementById("table-spinner");
    const tableBodyEl = document.getElementById("table-body");

    fetch("/provider", {
        method: "GET",
        headers: {"Content-Type": "application/json"}
    }).then(function(response){
        if (response.status === 200){
            return response.json();
        }else{
            tableSpinnerEl.style.display = "none";
        }

    }).then(function(jsonData){

    
        let content = "";
        let index = 0;
        for (let provider of jsonData){
            index += 1;
            content += tableContent(index, provider);
        }

        tableSpinnerEl.style.display = "none";
        tableBodyEl.innerHTML = content;
        listenToEditBtn();
        

    }).catch(function(err){
        tableSpinnerEl.style.display = "none";

    })


    

}

const tableContent = (index, provider) => {
    return `
            <tr>
                  <th scope="row">${index}</th>
                  <td>${provider.id}</td>
                  <td>${provider.name}</td>
                  <td style="width: 10px;">

                    <div class="btn-group" role="group" aria-label="action">
                        <button type="button" data-id="${provider.id}" data-name="${provider.name}" class="btn btn-primary  edit-data">edit</button>
                    </div>

                  </td>
            </tr>    
            `
}


const listenToEditBtn = () => {
    const editEls = document.querySelectorAll(".edit-data");
    editEls.forEach(function(element){
        element.onclick = function(event){
            const id = this.getAttribute("data-id")

            // load provider for update
            fetch(`/provider/${id}`,{
                method:"GET",
                headers: {"Content-Type": "application/jsons"}
            }).then(function(response){
                if (response.status === 200){
                    return response.json();
                }
            }).then(function(jsonData){

                const formContainerEl = document.querySelector("#form-container");
                const providerNameEl = document.querySelector("#provider-name");
                const cardFormTitleEl = document.querySelector("#card-form-title");
                const formEl = document.querySelector("#form");
                document.querySelector("#provider-name").value = jsonData.name;

                formContainerEl.style.display = "block";
                cardFormTitleEl.textContent = "Update Provider";
                providerNameEl.textContent = "";
                formEl.setAttribute("data-method-type", "PUT");
                formEl.setAttribute("data-endpoint", `/provider/${id}`);

            })

        }
    })

}