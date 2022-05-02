import React from "react";
import keplerGlReducer from "kepler.gl/reducers";
import { createStore, combineReducers, applyMiddleware } from "redux";
import { taskMiddleware } from "react-palm/tasks";
import { Provider, useDispatch } from "react-redux";
import KeplerGl from "kepler.gl";
import { addDataToMap } from "kepler.gl/actions";
import data from "../data/keplerMain.json";
import KeplerGlSchema from "kepler.gl/schemas";

const reducers = combineReducers({
  keplerGl: keplerGlReducer,
});

const store = createStore(reducers, {}, applyMiddleware(taskMiddleware));

export default function KeplerMap() {
  return (
    <Provider store={store}>
      <Map />
    </Provider>
  );
}

function Map() {
  const dispatch = useDispatch();
  React.useEffect(() => {
    const map1 = KeplerGlSchema.load(data);
    dispatch(addDataToMap(map1));
  }, [dispatch]);

  return (
    <KeplerGl
      id="map"
      mapboxApiAccessToken={
        "pk.eyJ1Ijoic2l3YXRjaGFpcmF0IiwiYSI6ImNsMmxibG9tZDAxcmgzY25ucjRzdmhpcjcifQ.DcT-GfJ1ThbJpH8xeP7xGw"
      }
      width={window.innerWidth}
      height={window.innerHeight}
    />
  );
}
