import App from './App.svelte'
import "jquery"
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap';

import { user } from './lib/stores';


const buildApp = () => {
  const app = new App({
    target: document.getElementById('app')
  })
}

fetch("/me")
  .then(resp => resp.json())
  .then(data => {
    user.set(data.data)
  })
  .finally(buildApp)