<script>
    import { writable } from "svelte/store";
    import { user } from "../lib/stores";
    import { SwalToast } from "../lib/helpers";
    import { onMount } from "svelte";

    const id = location.pathname.split("/").at(-1)

    let chatField;

    const messages = writable(null);

    const get_user = async () => {
        const details = [
            id
        ]

        const resp = await fetch("/getmessage", {
            method: "POST",
            body: JSON.stringify({details}),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await resp.json();
        $messages = data.data
    }
    onMount(get_user)
    
    function send_message(){
        const details = [
            recipient,
            chatField
        ]

        fetch("/sendmessage", {
            method: "POST",
            body: JSON.stringify({details}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(rep => rep.json()).then(data => {
            if (data["status"] === true){
                SwalToast.fire({
                    text: "Message sent",
                    icon: "success"
                })
            }
            else{
                SwalToast.fire({
                    text: "Error",
                    icon: "error"
                })
            }
        })
    }
    
    const get_msg = async () => {
        const details = [
            $user,
            10
        ]

        const resp = await fetch("/getmessage", {
            method: "POST",
            body: JSON.stringify({details}),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await resp.json();
        $messages = data.data
    }
    onMount(get_msg)
</script>

<form on:submit|preventDefault on:submit={send_message} id="loginform">
    <div class="form-outline mb-4">
        <input bind:value={chatField} type="text" id="icontent" class="form-control" />
    </div>

    <button type="submit" class="btn btn-primary btn-block mb-4">Send</button>
</form>