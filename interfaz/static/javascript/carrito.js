var updateBtns = documet.getElementsByClassName('agregar-carrito')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var nombreproducto = this.dataset.nombre
        var action = this.dataset.action
        console.log('Producto: ', nombreproducto, 'Accion: ', action)
    })
}