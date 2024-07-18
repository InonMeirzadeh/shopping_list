document.addEventListener('DOMContentLoaded', function() {
    const sortSelect = document.getElementById('sort-select');
    const productList = document.getElementById('product-list');

    sortSelect.addEventListener('change', function() {
        const sortBy = this.value;
        const products = Array.from(productList.children);

        products.sort((a, b) => {
            const aValue = a.textContent.split(' - ')[sortBy === 'name' ? 0 : 1];
            const bValue = b.textContent.split(' - ')[sortBy === 'name' ? 0 : 1];

            if (sortBy === 'name') {
                return aValue.localeCompare(bValue, 'he');
            } else {
                return parseInt(bValue) - parseInt(aValue);
            }
        });

        productList.innerHTML = '';
        products.forEach(product => productList.appendChild(product));
    });
});