<script>
    import Navbar from "../components/navbar.svelte"
    import { user } from "../lib/stores"
    import Chat from "../components/chat.svelte";
</script>

<Navbar />
<div class="container mt-4">
    <h1 class="text-center">Welcome, {$user.username}</h1>

    <Chat recipient={10} />
</div>

