package com.fabianrodriguez.nohit.hispano.backend.services.impl;

import com.fabianrodriguez.nohit.hispano.backend.services.defs.IGoogleService;
import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
import com.google.api.client.json.gson.GsonFactory;
import com.google.api.services.sheets.v4.Sheets;
import com.google.api.services.sheets.v4.model.ValueRange;
import com.google.auth.http.HttpCredentialsAdapter;
import com.google.auth.oauth2.GoogleCredentials;
import java.io.IOException;
import java.io.InputStream;
import java.security.GeneralSecurityException;
import java.util.List;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@Service
@Slf4j
@AllArgsConstructor
public class GoogleService implements IGoogleService {

	private static final GsonFactory JSON_FACTORY = GsonFactory.getDefaultInstance();
	private static final String SPREADSHEET_ID = "";

	public Sheets obtenerExcel() throws IOException, GeneralSecurityException {
		// Cargar credenciales desde el archivo JSON
		InputStream credentialsStream = GoogleService.class
				.getClassLoader()
				.getResourceAsStream("nohit-b62c6-310928f612b5.json");

		if (credentialsStream == null) {
			throw new IOException("No se pudo cargar el archivo de credenciales");
		}
		GoogleCredentials credentials = GoogleCredentials.fromStream(credentialsStream)
				.createScoped(List.of(""));

		return new Sheets.Builder(GoogleNetHttpTransport.newTrustedTransport(), JSON_FACTORY, new HttpCredentialsAdapter(credentials))
				.setApplicationName("")
				.build();
	}

	@Override
	public List<List<Object>> leerExcel() throws GeneralSecurityException, IOException {
		Sheets service = obtenerExcel();
		ValueRange response = service.spreadsheets().values()
				.get(SPREADSHEET_ID, "")
				.execute();

//		List<List<Object>> values = response.getValues();
//		if (values == null || values.isEmpty()) {
//			System.out.println("No se encontraron datos.");
//		} else {
//			for (List<Object> row : values) {
//				System.out.println(row); // Imprime cada fila de la hoja de cálculo
//			}
//		}
	}
}
