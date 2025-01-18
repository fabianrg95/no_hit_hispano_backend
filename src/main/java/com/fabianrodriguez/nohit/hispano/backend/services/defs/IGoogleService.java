package com.fabianrodriguez.nohit.hispano.backend.services.defs;

import java.io.IOException;
import java.security.GeneralSecurityException;
import java.util.List;

public interface IGoogleService {
	List<List<Object>> leerExcel(final String pagina) throws GeneralSecurityException, IOException;
}
