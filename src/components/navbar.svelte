<script>
    import { navigate } from "svelte-routing";
    import Swal from "sweetalert2";

    function logout(){
        fetch("/logout", {
            method: 'GET'
        })

        navigate("/login")
        Swal.fire({
            text: "Logged out",
            icon: "success",
            toast: true,
            position: "top-end",
            showConfirmButton: false,
            timer: 2000,
            timerProgressBar: true,
        });
    }
</script>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <div class="border-end mx-2">
            <span class="navbar-brand">chatsite</span>
        </div>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <a class="nav-link active mx-2" aria-current="page" href="/">Home</a>
                <a class="nav-link mx-2" href="/login">Login</a>
            </div>
        </div>
        <button type="button" on:click={logout} id="logoutbtn" class="mx-2 btn btn-danger">logout</button>
    </div>
</nav>