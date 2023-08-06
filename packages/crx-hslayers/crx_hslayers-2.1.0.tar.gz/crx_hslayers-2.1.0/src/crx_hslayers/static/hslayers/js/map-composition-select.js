const PROXY_PREFIX = "8087";  // "8010/proxy"
const SELECT_MAP_ID_POSTFIX = "-select";

class MapCompositionBlockDefinition extends window.wagtailStreamField.blocks.FieldBlockDefinition {
    slimSelects = {};

    render(placeholder, prefix, initialState, initialError) {
        const block = super.render(placeholder, prefix, initialState, initialError);
      const selectField = document.getElementById(prefix + SELECT_MAP_ID_POSTFIX);

        this.slimSelects[prefix] = new SlimSelect({
            select: selectField,
            allowDeselect: true,
            showOptionTooltips: true,
            onChange: this.onSelectionChange,
            addable: this.onValueAdded,
            searchPlaceholder: 'Search or enter URL'
        });

        fetch(this.getLaymanBaseUrl() + "/rest/maps")
            .then(response => response.json())
            .then(data => this.handleLaymanMaps(data, prefix))
            .catch(error => {
                console.error(error);
                this.handleLaymanMaps([], prefix);
            });

        return block;
    }

    getLaymanBaseUrl() {
        let origin = window.location.origin;
        if (origin.includes("localhost" | "127.0.0.1")) {
            console.warn("If you want to load Layman map compositions from local/development enviroment use local-cors-proxy (https://github.com/garmeeh/local-cors-proxy) to overcome CORS issues.");

            return origin.substring(0, origin.lastIndexOf(':') + 1) + PROXY_PREFIX;
        }

        return origin;
    }

    handleLaymanMaps(maps, inputId) {
        let inputValue = document.getElementById(inputId).value;
        let hasValueFromLayman = false;

        let options = maps.map(map => {
            let option = {
                text: map.title,
                value: map.url
            }

            if (map.url === inputValue) {
                hasValueFromLayman = true;
                option.selected = true;
            }

            return option;
        });

        if (!hasValueFromLayman && inputValue !== '') {
            options.unshift({
                text: inputValue,
                value: inputValue,
                selected: true,
            })
        }

        options.unshift({
            text: "Select or add map composition",
            placeholder: true
        })

        this.slimSelects[inputId].setData(options);
    }

    onValueAdded(value) {
        return value;
    }

    onSelectionChange(selectedOption) {
        let selectId = this.select.element.id;
      let input = document.getElementById(selectId.substring(0, selectId.lastIndexOf(SELECT_MAP_ID_POSTFIX)));
        input.value = selectedOption.value === "undefined" ? "" : selectedOption.value;
    }
}

window.telepath.register('hslayers.blocks.MapCompositionBlock', MapCompositionBlockDefinition);