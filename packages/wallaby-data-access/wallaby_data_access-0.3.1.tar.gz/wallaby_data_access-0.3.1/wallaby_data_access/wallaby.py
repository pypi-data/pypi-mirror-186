import os
import io
import sys
import csv
import glob
import logging
import secrets
import numpy as np
from dotenv import load_dotenv
import django
from django.db import models
from datetime import datetime
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from astropy.table import Table
from astropy.io.votable import from_table, writeto
from astropy.io.votable.tree import Param
from astropy.io import fits


logging.basicConfig(level=logging.INFO)


Run, Instance, Detection, Product, Source = None, None, None, None, None
SourceDetection, Comment, Tag, TagSourceDetection = None, None, None, None
Observation, ObservationMetadata, Tile, Postprocessing = None, None, None, None
KinematicModel, WKAPPProduct = None, None


def connect(
    db="/mnt/shared/wallaby/apps/WALLABY_database",
    env="/mnt/shared/wallaby/apps/WALLABY_data_access/wallaby_data_access/.env",
):
    """Establish connection to database through Django models.
    Need to specify path to database directory and .env file for Django settings environment variables.

    """
    global Run, Instance, Detection, Product, Source
    global SourceDetection, Comment, Tag, TagSourceDetection
    global Observation, ObservationMetadata, Tile, Postprocessing
    global KinematicModel, WKAPPProduct

    # Attempt to get database credentials from environment variables
    if 'WALLABY_DATABASE_PATH' in os.environ:
        db = os.environ['WALLABY_DATABASE_PATH']
    if 'WALLABY_DATABASE_CRED' in os.environ:
        env = os.environ['WALLABY_DATABASE_CRED']

    db_env = ['DATABASE_USER', 'DATABASE_PASS', 'DATABASE_HOST', 'DATABASE_NAME']
    if not os.path.exists(env):
        if any([os.getenv(e) is None for e in db_env]):
            logging.error("Input database credentials environment variable file not found.")
    else:
        load_dotenv(env)

    # Django environment variables
    os.environ["DJANGO_SECRET_KEY"] = secrets.token_urlsafe()
    os.environ["DJANGO_SETTINGS_MODULE"] = "orm.settings"
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "True"

    sys.path.append(db)
    sys.path.append(db + "/orm")
    django.setup()
    from source_finding.models import Run, Instance, Detection, Product, Source
    from source_finding.models import SourceDetection, Comment, Tag, TagSourceDetection
    from operations.models import Observation, ObservationMetadata, Tile, Postprocessing
    from kinematic_model.models import KinematicModel, WKAPPProduct

    return


def _write_bytesio_to_file(filename, bytesio):
    """Write the contents of the given BytesIO to a file.
    Creates the file or overwrites the file if it does
    not exist yet.

    """
    with open(filename, "wb") as outfile:
        # Copy the BytesIO stream to the output file
        outfile.write(bytesio.getbuffer())


def _write_zipped_fits_file(filename, product, compress=True):
    """Compress a .fits file as .fits.gz for a data product."""
    with io.BytesIO() as buf:
        buf.write(product)
        buf.seek(0)
        if not os.path.isfile(filename):
            _write_bytesio_to_file(filename, buf)
            if compress:
                os.system(f"gzip {filename}")


def _write_source_products(products, output_dir, name):
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_cube.fits"), products.cube
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_chan.fits"), products.chan
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_mask.fits"), products.mask
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_mom0.fits"), products.mom0
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_mom1.fits"), products.mom1
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_mom2.fits"), products.mom2
    )

    # Open spectrum
    with io.BytesIO() as buf:
        buf.write(b"".join(products.spec))
        buf.seek(0)
        spec_file = os.path.join(output_dir, f"{name}_spec.txt")
        if not os.path.isfile(spec_file):
            _write_bytesio_to_file(spec_file, buf)


def _write_kinematic_model_products(products, output_dir, name):
    """This currently writes the WKAPP Products to file."""
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_baroloinput.txt"), products.baroloinput
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_barolomod.txt"), products.barolomod
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_barolosurfdens.txt"), products.barolosurfdens
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_diagnosticplot.png"), products.diagnosticplot
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_diffcube.fits"), products.diffcube
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_fatinput.txt"), products.fatinput
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_fatmod.txt"), products.fatmod
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_fullresmodcube.fits"), products.fullresmodcube
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_fullresproccube.fits"),
        products.fullresproccube,
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_modcube.fits"), products.modcube
    )
    _write_zipped_fits_file(
        os.path.join(output_dir, f"{name}_procdata.fits"), products.procdata
    )


def get_slurm_output(source_name):
    """Get slurmOutput metadata for a given source
    TODO(austin): move into metadata submodule

    """
    source = Source.objects.get(name=source_name)
    sd = SourceDetection.objects.get(source=source)
    detection = Detection.objects.get(id=sd.detection_id)
    run = Run.objects.get(id=detection.run_id)
    postprocessing = Postprocessing.objects.get(run_id=run.id)
    tile = Tile.objects.get(identifier=postprocessing.name)
    obs_A = Observation.objects.get(id=tile.footprint_A.id)
    obs_B = Observation.objects.get(id=tile.footprint_B.id)
    meta_A = ObservationMetadata.objects.get(observation=obs_A)
    meta_B = ObservationMetadata.objects.get(observation=obs_B)
    return {
        str(obs_A.sbid): meta_A.__dict__["slurm_output"],
        str(obs_B.sbid): meta_B.__dict__["slurm_output"],
    }


# TODO(austin): some better descriptions
def get_primary_beam_correction_uses_holography(source_name):
    """Get beam processing information by parsing slurmOutput
    TODO(austin): move into metadata submodule

    """
    holography_keywords = ["ASKAP_PB_TT_IMAGE".lower(), "ASKAP_PB_CUBE_IMAGE".lower()]

    slurm_output = get_slurm_output(source_name)
    beam_info = {}
    for k, v in slurm_output.items():
        use_holography = all([hkw in v.keys() for hkw in holography_keywords])
        beam_info[k] = use_holography
    return beam_info


def get_catalog(tag):
    """Get catalogue for a given tag name as an astropy table"""
    tag = str(tag)
    if tag == "":
        sys.stderr.write(
            'Please specify a tag to extract a source catalogue, e.g.:\ntable = get_catalog(tag="NGC 5044 DR1")\n'
        )
        return None

    table = Table()

    # Get field names
    detection_field_names = [
        field.name
        for field in Detection._meta.fields
        if not isinstance(field, models.ForeignKey)
    ]
    detection_field_names.remove("name")
    detection_field_names.remove("access_url")
    detection_field_names.remove("access_format")
    detection_field_names.remove("unresolved")
    detection_field_names.remove("v_opt")
    detection_field_names.remove("v_app")
    detection_field_names.remove("v_rad")
    detection_field_names.remove("l")
    detection_field_names.remove("b")
    detection_field_names.remove("wm50")
    detection_field_names.remove("v_opt_peak")
    detection_field_names.remove("v_app_peak")
    detection_field_names.remove("v_rad_peak")
    detection_field_names.remove("l_peak")
    detection_field_names.remove("b_peak")
    detection_field_names.remove("x_peak")
    detection_field_names.remove("y_peak")
    detection_field_names.remove("z_peak")
    detection_field_names.remove("ra_peak")
    detection_field_names.remove("dec_peak")
    detection_field_names.remove("freq_peak")
    source_field_names = [
        field.name
        for field in Source._meta.fields
        if not isinstance(field, models.ForeignKey)
    ]
    source_field_names.remove("id")

    # Get sources and detections
    ir_tag = Tag.objects.get(name="Internal Release")
    sds = [
        tsd.source_detection
        for tsd in TagSourceDetection.objects.filter(
            tag_id=Tag.objects.get(name=tag).id
        )
    ]
    sds_released = [
        sd
        for sd in sds
        if ir_tag
        in [tsd.tag for tsd in TagSourceDetection.objects.filter(source_detection=sd)]
    ]
    sources = [sd.source for sd in sds_released]
    detections = [sd.detection for sd in sds_released]

    # Add columns to the table
    for field in source_field_names:
        if field == "name":
            table[field] = [getattr(s, field) for s in sources]
        else:
            table[field] = np.array([getattr(s, field) for s in sources], dtype=float)
    for field in detection_field_names:
        table[field] = np.array([getattr(d, field) for d in detections], dtype=float)

    # Extract and add comments, if any
    column_comments = []
    for i in range(len(table)):
        column_comments.append([])
        comments = Comment.objects.filter(detection=table["id"][i])
        for comment in comments:
            column_comments[i].append(comment.comment + " (" + comment.author + ")")
    table.add_column(col=column_comments, name="comments")

    # Extract and add tags, if any
    column_tags = []
    for i in range(len(table)):
        column_tags.append([])
        tags = TagSourceDetection.objects.filter(
            source_detection_id=SourceDetection.objects.get(detection_id=table["id"][i])
        )
        for t in tags:
            column_tags[i].append(Tag.objects.get(id=t.tag_id).name)
    table.add_column(col=column_tags, name="tags")

    # Extract team release column
    team_release = tag.replace("DR", "TR")
    column_team_release = [str(team_release)] * len(table)
    table.add_column(col=column_team_release, name="team_release")

    # Add additional properties
    c = 299792.458
    H0 = 70
    f0 = 1.420405751768e9
    dist_h = c * ((f0 / table["freq"]) - 1.0) / H0
    HI_mass = np.log10(49.7 * dist_h**2 * table["f_sum"])
    table.add_column(col=dist_h, name="dist_h")
    table.add_column(col=HI_mass, name="log_m_hi")

    return table


def save_products_for_source(id, filename, *args, **kwargs):
    """Save source finding output products for a given source name."""
    detection = Detection.objects.get(id=id)
    products = Product.objects.get(detection=detection)
    if not os.path.isdir(filename):
        os.mkdir(filename)

    # Write fits files
    _write_source_products(products, filename, detection.name.replace(" ", "_"))
    return


def save_source_products(table, filename, *args, **kwargs):
    """Save source finding output products for a given table"""
    if not os.path.isdir(filename):
        os.mkdir(filename)

    for row in table:
        id = int(row["id"])
        name = row["name"].replace(" ", "_")
        subdir = f"{filename}/{name}"
        if not os.path.isdir(subdir):
            os.mkdir(subdir)
        save_products_for_source(id, subdir)

    os.system(f"tar -czf {filename}.tar.gz {filename}")
    return


def save_products_for_kinematic_model(id, filename, *args, **kwargs):
    kinematic_model = KinematicModel.objects.get(id=id)
    products = WKAPPProduct.objects.get(kinematic_model=kinematic_model)
    if not os.path.isdir(filename):
        os.mkdir(filename)
    _write_kinematic_model_products(
        products, filename, kinematic_model.source.name.replace(" ", "_")
    )
    return


def save_kinematic_model_products(table, filename, *args, **kwargs):
    """Save kinematic modelling output products for a table"""
    if not os.path.isdir(filename):
        os.mkdir(filename)

    for row in table:
        id = int(row["id"])
        name = row["source"].replace(" ", "_")
        subdir = f"{filename}/{name}"
        if not os.path.isdir(subdir):
            os.mkdir(subdir)
        save_products_for_kinematic_model(id, subdir)

    os.system(f"tar -czf {filename}.tar.gz {filename}")
    return


# Print list of supported tags
def print_tags():
    tags = Tag.objects.all()
    for tag in tags:
        print("{:20s}\t{:s}".format('"' + tag.name + '"', tag.description))
    return


# Print list of kinematic model tags
def get_kinematic_model_tags():
    tr_tags = [k.team_release_kin for k in KinematicModel.objects.all()]
    return list(set(tr_tags))


def _get_kinematic_model_table(objects):
    table = Table()
    sources = [km.source for km in objects]
    columns = [f.name for f in KinematicModel._meta.fields]
    string_columns = ["team_release", "team_release_kin"]
    array_columns = [
        "rad",
        "vrot_model",
        "e_vrot_model",
        "e_vrot_model_inc",
        "rad_sd",
        "sd_model",
        "sd_fo_model",
        "e_sd_model",
        "e_sd_fo_model_inc",
    ]
    for field in columns:
        if field == "source":
            table[field] = np.array([s.name for s in sources], dtype=str)
        elif field in string_columns:
            table[field] = [getattr(k, field) for k in objects]
        elif field in array_columns:
            table[field] = [
                np.array([float(v) for v in getattr(k, field).split(",")])
                for k in objects
            ]
        elif field == "qflag_model":
            table[field] = np.array([getattr(k, field) for k in objects], dtype=int)
        else:
            table[field] = np.array([getattr(k, field) for k in objects], dtype=float)
    return table


# Generic function for getting kinematic models as astropy.Table
def get_kinematic_model(*args, **kwargs):
    res = KinematicModel.objects.filter(**kwargs)
    return _get_kinematic_model_table(res)


# Retrieve FITS image from database
def get_image(product):
    with io.BytesIO() as buf:
        buf.write(product)
        buf.seek(0)
        hdu = fits.open(buf)[0]
        return hdu.data, hdu.header


# Retrieve spectrum from database
def get_spectrum(product):
    with io.BytesIO() as buf:
        buf.write(b"".join(product))
        buf.seek(0)
        return np.loadtxt(buf, dtype="float", comments="#", unpack=True)


# Create overview plot
def overview_plot(id, size=(8, 6)):
    # Retrieve products from database
    detection = Detection.objects.get(id=id)
    products = Product.objects.get(detection=detection)
    plot = products.plot
    if plot is None:
        logging.error(f"No summary plot for detection {detection.name}")
        return None

    fig, ax = plt.subplots(nrows=1, ncols=1)
    fig.set_size_inches(*size)
    img = mpimg.imread(io.BytesIO(plot))
    plt.imshow(img)
    plt.axis("off")
    plt.tight_layout()
    ax = plt.gca()
    ax.set_frame_on(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    return plt


def save_overview(tag, *args, **kwargs):
    """Save overview plots for tagged sources"""
    table = get_catalog(tag)
    parent = "%s_overview" % tag.replace(" ", "_")
    if not os.path.isdir(parent):
        os.mkdir(parent)

    for row in table:
        name = row["name"].replace(" ", "_")
        p = overview_plot(row["id"])
        p.savefig(f"{parent}/{name}_overview.png")
        p.close()

    os.system(f"tar -czf {parent}.tar.gz {parent}")

    return


def save_spectrum(detection, filename):
    products = Product.objects.get(detection=detection)
    spectrum = products.spec

    # store spectrum as numpy array
    array = []
    with io.BytesIO() as buf:
        buf.write(b"".join(products.spec))
        buf.seek(0)
        text = buf.getbuffer().tobytes().decode("utf-8")
        lines = text.strip().split("\n")
        for line in lines:
            if not line.startswith("#"):
                chan, freq, flux, pix = line.strip().split()
                array.append(np.array([int(chan), float(freq), float(flux), int(pix)]))
    array = np.array(array)

    # write to fits file
    t = Table(
        array,
        names=("Channel", "Frequency", "Flux Density", "Pixels"),
        dtype=(int, np.float32, np.float32, int),
    )
    t.write(filename, format="fits")

    # update spectrum metadata
    spectrum = fits.open(filename, "update")
    spectrum[0].data = np.array([[[0]]]).astype("int16")
    hdr = spectrum[0].header
    hdr["WCSAXES"] = 3
    hdr["CRPIX1"] = 0
    hdr["CRPIX2"] = 0
    hdr["CRPIX3"] = 0
    hdr["CDELT1"] = -0.00166666
    hdr["CDELT2"] = 0.00166666
    hdr["CDELT3"] = 18518.0
    hdr["CUNIT1"] = "deg"
    hdr["CUNIT2"] = "deg"
    hdr["CUNIT3"] = "Hz"
    hdr["CTYPE1"] = "RA---SIN"
    hdr["CTYPE2"] = "DEC--SIN"
    hdr["CTYPE3"] = "FREQ"
    hdr["CRVAL1"] = detection.ra
    hdr["CRVAL2"] = detection.dec
    hdr["CRVAL3"] = detection.freq

    # Provenance metadata
    hdr["SBID"] = ""
    hdr["SRCVER"] = ""
    hdr["SRCTR"] = ""
    hdr["DATE"] = datetime.now().isoformat()

    spectrum.close()
    return


def casda_deposit(table, deposit_name):
    """Export source data products and catalogue for Astropy table for CASDA release.
    Will create an output directory with the deposit name and store products in that folder.

    """
    # ensure output directory exists
    if not os.path.exists(deposit_name):
        os.mkdir(deposit_name)
    else:
        raise Exception("Output directory exists but is not empty.")

    # subdirectories
    os.mkdir(f"{deposit_name}/catalogue")
    os.mkdir(f"{deposit_name}/cubelets")
    os.mkdir(f"{deposit_name}/spectra")
    os.mkdir(f"{deposit_name}/moment_maps")
    os.mkdir(f"{deposit_name}/plots")

    # Export products
    for row in table:
        name = row["name"].replace(" ", "_")
        release = row["team_release"].replace(" ", "_")
        detection = Detection.objects.get(id=row["id"])
        products = Product.objects.get(detection=detection)
        filename_prefix = f"{name}_{release}"

        # write .fits files
        _write_zipped_fits_file(
            "%s/%s/%s_cube.fits" % (deposit_name, "cubelets", filename_prefix),
            products.cube,
            compress=False,
        )  # noqa
        _write_zipped_fits_file(
            "%s/%s/%s_chan.fits" % (deposit_name, "moment_maps", filename_prefix),
            products.chan,
            compress=False,
        )  # noqa
        _write_zipped_fits_file(
            "%s/%s/%s_mask.fits" % (deposit_name, "cubelets", filename_prefix),
            products.mask,
            compress=False,
        )  # noqa
        _write_zipped_fits_file(
            "%s/%s/%s_mom0.fits" % (deposit_name, "moment_maps", filename_prefix),
            products.mom0,
            compress=False,
        )  # noqa
        _write_zipped_fits_file(
            "%s/%s/%s_mom1.fits" % (deposit_name, "moment_maps", filename_prefix),
            products.mom1,
            compress=False,
        )  # noqa
        _write_zipped_fits_file(
            "%s/%s/%s_mom2.fits" % (deposit_name, "moment_maps", filename_prefix),
            products.mom2,
            compress=False,
        )  # noqa
        save_spectrum(
            detection, "%s/%s/%s_spec.fits" % (deposit_name, "spectra", filename_prefix)
        )

        # add source name to each header file
        product_files = glob.glob(f"{deposit_name}/{name}_{release}*.fits")
        for f in product_files:
            hdul = fits.open(f, "update")
            hdr = hdul[0].header
            hdr["WALTR"] = release
            hdul.close()

        # TODO: add SDIBs to WALSBID header cards

        # TODO: add moment 0 maps (png) to products under separate folder
        mom0, _ = get_image(products.mom0)
        plt.imshow(mom0)
        plt.axis("off")
        plt.savefig("%s/%s/%s_mom0.png" % (deposit_name, "plots", filename_prefix))
        plt.close()

    # Read columns and metadata
    table_columns = {}
    module_path = os.path.dirname(os.path.abspath(__file__))
    with open(f"{module_path}/source_column_metadata.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, ucd, units, description = row
            units = units.replace("pixel", "pix")
            if units == "-":
                units = None
            table_columns[name] = (ucd, units, description)

    # Export catalogue
    column_names = [k for k in table_columns.keys()]
    table.remove_column("id")
    table.remove_column("tags")
    table = table[column_names]
    votable = from_table(table)
    votable.version = "1.3"

    # Update fields
    fields = []
    for name, meta in table_columns.items():
        ucd, units, description = meta
        field = votable.get_field_by_id(name)
        field.ucd = ucd
        field.unit = units
        field.description = description
        fields.append(field)
        if field.datatype == "unicodeChar":
            field.datatype = "char"

    for resource in votable.resources:
        # update rows
        for t in resource.tables:
            for i, row in enumerate(fields):
                t.fields[i] = row

            # add params
            t.params.append(
                Param(
                    votable,
                    ID="catalogueName",
                    name="Catalogue Name",
                    value=deposit_name,
                    arraysize="59",
                )
            )  # noqa
            t.params.append(
                Param(
                    votable,
                    ID="indexedFields",
                    name="Indexed Fields",
                    value="name,ra,dec,freq,f_sum,w20,team_release",
                    arraysize="255",
                )
            )  # noqa
            t.params.append(
                Param(
                    votable,
                    ID="principalFields",
                    name="Principal Fields",
                    value="name,ra,dec,freq,f_sum,w20,team_release",
                    arraysize="255",
                )
            )  # noqa

    catalogue_file = f"{deposit_name}/catalogue/catalogue.xml"
    writeto(votable, catalogue_file)

    return
