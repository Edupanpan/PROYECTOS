import React, { useState, useEffect, useCallback } from 'react';
import { GoogleMap, useJsApiLoader, MarkerF } from '@react-google-maps/api';
import axios from 'axios'; // Importamos Axios
import { Container } from 'react-bootstrap'; 
const containerStyle = {
    width: '1000px',
    height: '700px',
  }
  
  const center = {
    lat: -3.745,
    lng: -38.523,
  }

function MyComponent() {
    const { isLoaded } = useJsApiLoader({
        id: 'google-map-script',
        googleMapsApiKey: 'AIzaSyBv4CZG5cyoF4wPerFfIAk7CsTMBranGZM',
        libraries: ['places'], // Aseguramos que cargue la librería 'places'
    });

    const [map, setMap] = useState(null);
    const [lugares, setLugares] = useState([]); // Guardamos los lugares encontrados
    const [direccion, setDireccion] = useState(''); // Estado para la dirección de búsqueda
    const [marcador, setMarcador] = useState(null); // Estado para el marcador de búsqueda

    // Función para buscar lugares por texto utilizando la API de Places
    const buscarLugarPorTexto = (texto) => {
        return new Promise((resolve, reject) => {
            if (!map) return reject('Mapa no cargado');

            const service = new window.google.maps.places.PlacesService(map);

            const request = {
                query: texto,
                fields: ['name', 'geometry', 'formatted_address'],
            };

            service.textSearch(request, (results, status) => {
                if (status === window.google.maps.places.PlacesServiceStatus.OK) {
                    resolve(results[0]); // Retornamos solo el primer resultado relevante
                } else {
                    console.error(`Error en la búsqueda por texto: ${status}`);
                    resolve(null); // Evitamos que la promesa falle si no hay resultados
                }
            });
        });
    };

    // Obtener datos desde MockAPI y buscar cada dirección usando la API de Places
    const obtenerDatos = async () => {
        try {
            const response = await axios.get('https://66fd61c7699369308954fd8e.mockapi.io/lugares/visita');
            const lugaresEncontrados = await Promise.all(
                response.data.map(async (lugar) => {
                    const resultado = await buscarLugarPorTexto(lugar.direccion);
                    return resultado ? { ...lugar, coordenadas: resultado.geometry.location } : null;
                })
            );

            // Filtramos los lugares que no se encontraron
            setLugares(lugaresEncontrados.filter((lugar) => lugar !== null));
        } catch (error) {
            console.error('Error al obtener los datos:', error);
        }
    };

    useEffect(() => {   
        if (isLoaded) {
            obtenerDatos(); // Ejecutamos la búsqueda al cargar el mapa
        }
    }, [isLoaded]);

    const onLoad = useCallback((map) => {
        const bounds = new window.google.maps.LatLngBounds(center);
        map.fitBounds(bounds);
        setMap(map);
    }, []);

    const onUnmount = useCallback(() => {
        setMap(null);
    }, []);

    const handleBuscar = async () => {
        const resultado = await buscarLugarPorTexto(direccion);
        if (resultado) {
            setMarcador({
                position: resultado.geometry.location,
                title: resultado.formatted_address,
            });
        }
    };

    return isLoaded ? (
        <>

            <Container className='d-flex flex-column vh-100 align-items-center '>
                <h2>Direcciones de los Lugares:</h2>
                <GoogleMap
                    mapContainerStyle={containerStyle}
                    center={center}
                    zoom={12}
                    onLoad={onLoad}
                    onUnmount={onUnmount}
                    options={{
                        streetViewControl: false,
                    }}
                >
                    {/* Marcadores para cada lugar encontrado */}
                    {lugares.map((lugar) => (
                        <MarkerF
                            key={lugar.id}
                            position={lugar.coordenadas}
                            title={lugar.direccion}
                        />
                    ))}
                    {/* Marcador de búsqueda */}
                    {marcador && (
                        <MarkerF
                            position={marcador.position}
                            title={marcador.title}
                        />
                    )}
                </GoogleMap>

            </Container>
        </>
    ) : (
        <></>
    );
}

export default React.memo(MyComponent);
