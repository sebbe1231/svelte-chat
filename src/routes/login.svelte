<script>
    import Swal from "sweetalert2";
    import { navigate } from "svelte-routing";
    import { user } from "../lib/stores"
    import Register from "../components/register.svelte"

    let name;
    let pass;

    function loginfunc(){
        const details = [
            name,
            pass
        ];

        fetch("/logincheck", {
            method: "POST",
            body: JSON.stringify({details}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(rep => rep.json()).then(data => {
            if (data["status"] === true) {
                user.set(name)
                navigate("/")

                Swal.fire({
                    text: "Logged in",
                    icon: "success",
                    toast: true,
                    position: "top-end",
                    showConfirmButton: false,
                    timer: 2000,
                    timerProgressBar: true,
                });
            }
            else {
                Swal.fire({
                    text: "Wrong login",
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

<div class="container mt-4">
    <Register />
    <form on:submit|preventDefault on:submit={loginfunc} id="loginform">
        <div class="form-outline mb-4">
            <input bind:value={name} type="text" id="loginname" class="form-control" />
            <label class="form-label" for="loginname">Username</label>
        </div>
    
        <div class="form-outline mb-4">
            <input bind:value={pass} type="password" id="loginpass" class="form-control" />
            <label class="form-label" for="loginpass">Password</label>
        </div>

        <button type="submit" class="btn btn-primary btn-block mb-4">Sign in</button>
        <button type="button" class="btn btn-secondary btn-block mb-4" data-bs-toggle="modal" data-bs-target="#registerModal">Register</button>
    </form>
</div>