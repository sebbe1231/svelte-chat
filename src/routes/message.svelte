<script>
    import { writable } from "svelte/store";
    import { user } from "../lib/stores";
    import { SwalToast } from "../lib/helpers";
    import { onMount } from "svelte";
    import Navbar from "../components/navbar.svelte"

    const id = location.pathname.split("/").at(-1)

    let chatField;

    const messages = writable(null);
    const recepiant = writable(null);

    const get_user = async () => {
        const details = [
            null,
            id
        ]

        const resp = await fetch("/getuser", {
            method: "POST",
            body: JSON.stringify({details}),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await resp.json();
        $recepiant = data.data;
    }
    onMount(get_user)
    
    function send_message(){
        const details = [
            id,
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
            id,
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
        $messages = data.data.reverse()
    }
    onMount(get_msg)
</script>

<div class="wp">
    <Navbar />
    <div class="container mt-4">
        <div class="d-flex flex-column">
            <h1>{$recepiant?.username}</h1>
            <div class="border align-self-stretch text-area">
                <ul class="list-group">
                    {#if $messages}
                        {#each $messages as msg}
                            {#if msg[1] == id && $user.id != id}
                                <li class="list-group-item list-group-item-secondary">
                                    <div class="d-flex w-100 justify-content-between">
                                        <h5 class="mb-1">{$recepiant.username} ({$recepiant.id})</h5>
                                        <small>{msg[4]}</small>
                                    </div>
                                    <p class="mb-1">{msg[3]}</p>
                                </li>
                            {:else}
                                <li class="list-group-item list-group-item-primary">
                                    <div class="d-flex w-100 justify-content-between">
                                        <h5 class="mb-1">{$user.username} ({$user.id})</h5>
                                        <small>{msg[4]}</small>
                                    </div>
                                    <p class="mb-1">{msg[3]}</p>
                                </li>
                            {/if}
                        {/each}
                    {/if}
                </ul>
            </div>
            <div class="sticky-bottom bg-light">
                <form on:submit={send_message} id="loginform">
                    <div class="input-group mb-3">
                        <!-- svelte-ignore a11y-autofocus -->
                        <input bind:value={chatField} type="text" id="msgcontent" class="form-control" placeholder="What do you want to say?" autofocus />
                        <button type="submit" class="btn btn-primary">Send</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>