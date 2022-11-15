<script>
    import Navbar from "../components/navbar.svelte"
    import { user } from "../lib/stores"
</script>

<Navbar />
<h1 class="text-center">Welcome, {$user}</h1>