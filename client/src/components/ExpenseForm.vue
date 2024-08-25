<template>
<div class="exp-form">
    <div class="col-12">
        <h5>Add Expense:</h5>
    </div>
    <form class="row g-2" @submit.prevent="addExpense">
        <div class="col-12">
            <input type="text" class="form-control" v-model="purchase" placeholder="Purchase" required />
        </div>
        <div class="col-12">
            <div class="input-group">
                <div class="input-group-text">$</div>
                <input type="number" class="form-control" v-model.number="amount" step="0.01" id="autoSizingInputGroup" placeholder="Amount" required>
            </div>
        </div>
        <div class="col-12">
            <select class="form-select" v-model.number="importance" required>
                <option disabled value="0">Importance...</option>
                <option value="1">Not at all</option>
                <option value="2">somewhat</option>
                <option value="3">Necessity</option>
            </select>
        </div>
        <div class="col-12">
            <input type="date" v-model="date" required />
        </div>
        <div class="col-12">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="recurringCheck" v-model="isRecurring">
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

<script>
import axios from 'axios';

export default {
    data() {
        return {
            purchase: '',
            amount: 0.0,
            importance: 0,
            date: '',
            isRecurring: false,
        };
    },
    methods: {
        async addExpense() {

            const id = 1;

            // get date's unix timestamp
            const dateTimestamp = new Date(this.date).getTime() / 1000;

            try {
                const resp = await axios.post('http://localhost:3000/exp', {
                    user_id: id,
                    purchase: this.purchase,
                    amount: this.amount,
                    importance: this.importance,
                    date: dateTimestamp
                });
                console.log(resp.data.id);

            } catch (err) {
                console.log(err.message);
            }
        }
    }
}


</script>

<style>

.exp-form {
    width: 375px;
    padding: 20px;
}

</style>