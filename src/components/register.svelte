<!-- Where a modal will pop up for registration -->
<script>
    // First check of username already exists
    // then make account, if username dosent exists, otherwise show error
    // if account created, show success and redirect to root
    
</script>

<div class="modal fade" id="registerModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5">Register account</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form on:submit|preventDefault id="regform">
                    <div class="form-outline mb-4">
                        <input type="text" id="regname" class="form-control" />
                        <label class="form-label" for="regname">Username</label>
                    </div>
                
                    <div class="form-outline mb-4">
                        <input type="password" id="regpass" class="form-control" />
                        <label class="form-label" for="regpass">Password</label>
                    </div>

                    <div class="form-outline mb-4">
                        <input type="password" id="regpass" class="form-control" />
                        <label class="form-label" for="regpass">Confirm password</label>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                <button type="button" class="btn btn-primary">Submit</button>
            </div>
        </div>
    </div>
</div>