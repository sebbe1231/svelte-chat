<!-- Where a modal will pop up for registration -->
<script>
    import Swal from "sweetalert2"
    import { navigate } from "svelte-routing";
    import jquery from "jquery";

    let name;
    let pass;

    function registerUser(){
        const details = [
            name,
            pass
        ]

        fetch("/register", {
            method: "POST",
            body: JSON.stringify({details}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(rep => rep.json()).then(data => {
            if (data["status"] === true) {
                navigate("/");
                jquery(".modal-backdrop").remove()

                Swal.fire({
                    text: "Account created",
                    icon: "success",
                    toast: true,
                    position: "top-end",
                    showConfirmButton: false,
                    timer: 2000,
                    timerProgressBar: true,
                });
            }
            else{
                Swal.fire({
                    text: "Username already exists",
                    icon: "error",
                    toast: true,
                    position: "top-end",
                    showConfirmButton: false,
                    timer: 2000,
                    timerProgressBar: true,
                });
            }
        })
    }
    
</script>

<div class="modal fade" id="registerModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <form on:submit|preventDefault on:submit={registerUser} id="regform">
                <div class="modal-header">
                    <h1 class="modal-title fs-5">Register account</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="form-outline mb-4">
                        <input bind:value={name} type="text" id="regname" class="form-control" />
                        <label class="form-label" for="regname">Username</label>
                    </div>
                
                    <div class="form-outline mb-4">
                        <input bind:value={pass} type="password" id="regpass" class="form-control" />
                        <label class="form-label" for="regpass">Password</label>
                    </div>

                    <div class="form-outline mb-4">
                        <input type="password" id="regpasscon" class="form-control" />
                        <label class="form-label" for="regpass">Confirm password</label>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    <button type="submit" class="btn btn-primary">Submit</button>
                </div>
            </form>
        </div>
    </div>
</div>