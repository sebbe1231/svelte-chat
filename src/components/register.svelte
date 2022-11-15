<!-- Where a modal will pop up for registration -->
<script>
    import Swal from "sweetalert2"
    import { navigate } from "svelte-routing";
    import { user } from "../lib/stores"
    import jquery from "jquery";

    let name;
    let pass;
    let passcon;

    const Toast = Swal.mixin({
        toast: true,
        position: "top-end",
        showConfirmButton: false,
        timer: 2000,
        timerProgressBar: true,
    })

    function registerUser(){
        if (pass !== passcon){
            return Toast.fire({
                text: "Passwords do not match",
                icon: "error"
            })
        }
        if(pass === undefined || name === undefined){
            return Toast.fire({
                text: "Error",
                icon: "error"
            });
        }

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
                user.set(name)
                navigate("/");

                // Bit cursed, but the modal backdrop stayes on route for some reason, so i have to delete it
                jquery(".modal-backdrop").remove()

                Toast.fire({
                    text: "Account created",
                    icon: "success",
                });
            }
            else{
                Toast.fire({
                    text: "Username already exists",
                    icon: "error",
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
                        <input bind:value={passcon} type="password" id="regpasscon" class="form-control" />
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