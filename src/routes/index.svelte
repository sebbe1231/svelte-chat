<script>
    import Navbar from "../components/navbar.svelte"
    import { user } from "../lib/stores"
    import Swal from "sweetalert2"
    import { get } from "svelte/store";

    let reciver;
    let content;

    const Toast = Swal.mixin({
        toast: true,
        position: "top-end",
        showConfirmButton: false,
        timer: 2000,
        timerProgressBar: true,
    })

    

    function send_message(){
        const details = [
            reciver,
            content
        ]

        fetch("/sendmessage", {
            method: "POST",
            body: JSON.stringify({details}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(rep => rep.json()).then(data => {
            if (data["status"] === true){
                Toast.fire({
                    text: "Message sent",
                    icon: "success"
                })
            }
            else{
                Toast.fire({
                    text: "Error",
                    icon: "error"
                })
            }
        })
    }
</script>

<Navbar />
<div class="container mt-4">
    <h1 class="text-center">Welcome, {$user}</h1>

    <form on:submit|preventDefault on:submit={send_message} id="loginform">
        <div class="form-outline mb-4">
            <input bind:value={reciver} type="text" id="ireciver" class="form-control" />
            <label class="form-label" for="ireciver">Who will you send it to?</label>
        </div>
    
        <div class="form-outline mb-4">
            <input bind:value={content} type="text" id="icontent" class="form-control" />
            <label class="form-label" for="icontent">Message content</label>
        </div>

        <button type="submit" class="btn btn-primary btn-block mb-4">Send</button>
    </form>
    <ul class="list-group">
        <li class="list-group-item">lol</li>
    </ul>
</div>

