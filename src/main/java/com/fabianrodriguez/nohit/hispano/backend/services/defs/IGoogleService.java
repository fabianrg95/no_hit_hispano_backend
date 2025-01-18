package com.fabianrodriguez.nohit.hispano.backend.services.defs;

import com.google.api.services.sheets.v4.Sheets;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.security.GeneralSecurityException;

public interface IGoogleService {
	void leerExcel() throws GeneralSecurityException, IOException;
}
