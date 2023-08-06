const PROXY_URL = "http://localhost:8085/";
const EPSG_API_BASE_URL =
  "https://apps.epsg.org/api/v1/CoordRefSystem/?keywords=";
const SELECT_PROJ_ID_POSTFIX = "-select";

class MapProjectionBlockDefinition extends window.wagtailStreamField.blocks
  .FieldBlockDefinition {
  slimSelects = {};

  render(placeholder, prefix, initialState, initialError) {
    const block = super.render(placeholder, prefix, initialState, initialError);
    const selectField = document.getElementById(prefix + SELECT_PROJ_ID_POSTFIX);

    this.slimSelects[prefix] = new SlimSelect({
      select: selectField,
      allowDeselect: true,
      showOptionTooltips: true,
      ajax: function (search, callback) {
        if (search.length < 3) {
          callback("At least 3 charactes are needed to search...");
          return;
        }

        let url = EPSG_API_BASE_URL + search;
        if (origin.indexOf("localhost") > 0)
          url = PROXY_URL + url;

        fetch(url, {
          headers: {
            Accept: "application/json",
          },
        })
          .then((response) => response.json())
          .then((data) => {
            let selectItems = data.Results.map(item => {
              let option = {
                text: `${item.Name} (${item.DataSource}:${item.Code})`,
                value: `${item.DataSource}:${item.Code}`
              }

              return option;
            });

            callback(selectItems);
          })
          .catch((error) => {
            console.error(error);
          });
      },
      searchPlaceholder: "Search CRS",
    });

    return block;
  }
}

window.telepath.register(
  "hslayers.blocks.MapProjectionBlock",
  MapProjectionBlockDefinition
);
