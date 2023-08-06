define([
  'base/js/namespace'
], function(
  Jupyter
){
  let NBList = Jupyter.notebook_list;
  let name_sorter = NBList.sort_function;

  function sort_function(a, b) {
    if (a['type'] != b['type'])
      return name_sorter(a, b);

    let aIndex = NBList._file_order.order.indexOf(a['name']);
    let bIndex = NBList._file_order.order.indexOf(b['name']);
    if (aIndex > -1 && bIndex > -1)
      return aIndex < bIndex ? -1 : 1;
    else if (aIndex > -1)
      return -1;
    else if (bIndex > -1)
      return 1;
    return name_sorter(a, b);
  }

  function sort_handler() {
    // Clear sort indications
    $('.sort-action i').removeClass('fa-arrow-up').removeClass('fa-arrow-down');
    $('#custom-sort i').addClass('fa-arrow-down');

    NBList.sort_function = sort_function;
    NBList.draw_notebook_list(NBList.model_list, NBList.error_msg);
    NBList.sort_id = 'custom-sort';
  }

  async function get_file_order() {
    let order_file = `${NBList.base_url}customorder/${NBList.notebook_path}`.replace('//', '/');
    try {
      let response = await fetch(order_file);
      if (!response.ok)
        throw new Error('Fetch of file order failed', {cause: response.status});

      NBList._file_order = await response.json();
      $('#custom_sort').show();
      sort_handler();
    } catch(error) {
      NBList._file_order = undefined;
      $('#custom_sort').hide();
      if (NBList.sort_id === 'custom-sort')
        $('#sort-name').click();
      if (error.cause !== 404)
        console.log(error);
    }
  }

  function load_ipython_extension() {
    let buttonContainer = document.querySelector('#sort_buttons');
    buttonContainer.insertAdjacentHTML('afterbegin', `
      <div id="custom_sort" class="sort_button" style="display: none;">
        <button id="custom-sort" class="btn btn-xs btn-default sort-action" type="button" aria-label="Custom Sort">
          Custom
          <i class="fa"></i>
        </button>
      </div>
    `);
    $('#custom-sort').click(sort_handler);

    let old_load_list = NBList.load_list;
    NBList.load_list = function() {
      // Correctly binds this in the old function
      old_load_list.apply(NBList);
      get_file_order();
    };
    get_file_order();
  }

  return {
    load_ipython_extension: load_ipython_extension
  };
})
