// # ----------------------------------------------
// # --------
// #
// # Cluster and Cloud Computing Assignment 2 - Team 53
// #
// # Authors:
// # - Chi Yin Wong (Student ID: 836872)
// # - Kaiquan Lin (Student ID: 1147233)
// # - Renkai Liao (Student ID: 1141584)
// # - Renwei Hu (Student ID: 1067974)
// # - Siwat Chairattanamanokorn (Student ID: 1338152)
// #
// # Author of this file:
// # - Siwat Chairattanamanokorn (Student ID: 1338152)
// #
// # Location:
// # - Melbourne
// #
// # --------
// # ----------------------------------------------

import React from "react";
import { keplerGlReducer, uiStateUpdaters } from "kepler.gl/reducers";
import { createStore, combineReducers, applyMiddleware } from "redux";
import { taskMiddleware } from "react-palm/tasks";
import { Provider, useDispatch } from "react-redux";
import { KeplerGl, Redux } from "kepler.gl";
import { addDataToMap } from "kepler.gl/actions";
import data from "../data/testData/crime/kepler/family_violence_kepler.json";
import KeplerGlSchema from "kepler.gl/schemas";
import AutoSizer from "react-virtualized/dist/commonjs/AutoSizer";

const reducers = (function createReducers(Redux, KeplerGl) {
  const customizedKeplerGlReducer = keplerGlReducer.initialState({
    uiState: {
      readOnly: true,
      mapControls: {
        ...uiStateUpdaters.DEFAULT_MAP_CONTROLS,
        visibleLayers: {
          show: false,
        },
        mapLegend: {
          show: true,
          active: true,
        },
      },
    },
  });
  return combineReducers({
    // mount keplerGl reducer
    keplerGl: customizedKeplerGlReducer,
  });
})(Redux, KeplerGl);

const store = createStore(reducers, {}, applyMiddleware(taskMiddleware));

export default function KeplerMapViolence() {
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
    <div style={{ position: "absolute", width: "100%", height: "100%" }}>
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
