import App from './App.svelte'
import "jquery"
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap';

const app = new App({
  target: document.getElementById('app')
})

export default app
