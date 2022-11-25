<script>
    import Navbar from "../components/navbar.svelte"
    import { user } from "../lib/stores"
    import Chat from "../components/chat.svelte";
    import { navigate } from "svelte-routing";

    let recipient;

    function redirect_message(){
        const details = [
            recipient
        ]

        console.log(recipient)

        fetch("/getuser", {
            method: "POST",
            body: JSON.stringify({details}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(rep => rep.json()).then(data => {
            navigate(`/message/${data.data[0]}`)
        })
    }
</script>

<Navbar />
<div class="container mt-4">
    <h1 class="text-center">Welcome, {$user.username}</h1>

    <form on:submit|preventDefault on:submit={redirect_message} id="loginform">
        <div class="form-outline mb-4">
            <label class="form-label" for="ireciver">Who will you send it to?</label>
            <input bind:value={recipient} type="text" id="ireciver" class="form-control" />
        </div>
    </form>

</div>

