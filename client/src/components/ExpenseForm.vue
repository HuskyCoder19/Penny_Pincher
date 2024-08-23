<template>
<div class="exp-form">
    <div class="col-12">
        <h5>Add Expense:</h5>
    </div>
    <form class="row g-2">
        <div class="col-12">
            <input type="text" class="form-control" placeholder="Purchase">
        </div>
        <div class="col-12">
            <div class="input-group">
                <div class="input-group-text">$</div>
                <input type="text" class="form-control" id="autoSizingInputGroup" placeholder="Amount">
            </div>
        </div>
        <div class="col-12">
            <select class="form-select">
                <option selected>Importance...</option>
                <option value="1">Not at all</option>
                <option value="2">somewhat</option>
                <option value="3">Very</option>
            </select>
        </div>
        <div class="col-12">
            <div class="form-date">
                <input class="form-date-input" type="date">
            </div>
        </div>
        <div class="col-12">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="recurringCheck">
                <label class="form-check-label" for="recurringCheck">
                    Recurring
                </label>
            </div>
        </div>
        <div class="col-12">
            <button type="submit" class="btn btn-primary">Add</button>
        </div>
    </form>
</div>
</template>

<style>

.exp-form {
    width: 375px;
    padding: 20px;
}

</style>