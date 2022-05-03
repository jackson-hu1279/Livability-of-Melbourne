import React from "react";
import keplerGlReducer from "kepler.gl/reducers";
import { createStore, combineReducers, applyMiddleware } from "redux";
import { taskMiddleware } from "react-palm/tasks";
import { Provider, useDispatch } from "react-redux";
import { KeplerGl, Redux } from "kepler.gl";
import { addDataToMap } from "kepler.gl/actions";
import data from "../data/testData/crime/family_violence_kepler.json";
import KeplerGlSchema from "kepler.gl/schemas";
import AutoSizer from "react-virtualized/dist/commonjs/AutoSizer";

const reducers = (function createReducers(redux, keplerGl) {
  const customizedKeplerGlReducer = keplerGlReducer.initialState({
    uiState: { readOnly: true },
  });
  return combineReducers({
    // mount keplerGl reducer
    keplerGl: customizedKeplerGlReducer,
  });
})(Redux, KeplerGl);

const store = createStore(reducers, {}, applyMiddleware(taskMiddleware));

export default function KeplerMapHistoricCrime() {
  return (
    <Provider store={store}>
      <Map />
    </Provider>
  );
}

function Map() {
  const dispatch = useDispatch();

  React.useEffect(() => {
    const map = KeplerGlSchema.load(data);
    store.dispatch(addDataToMap(map, { readOnly: true }));
  }, [dispatch]);

  return (
    <div style={{ position: "absolute", width: "50%", height: "50%" }}>
      <AutoSizer>
        {({ height, width }) => (
          <KeplerGl
            mapboxApiAccessToken={
              "pk.eyJ1Ijoic2l3YXRjaGFpcmF0IiwiYSI6ImNsMmxibG9tZDAxcmgzY25ucjRzdmhpcjcifQ.DcT-GfJ1ThbJpH8xeP7xGw"
            }
            id="map"
            width={width}
            height={height}
          />
        )}
      </AutoSizer>
    </div>
  );
}
