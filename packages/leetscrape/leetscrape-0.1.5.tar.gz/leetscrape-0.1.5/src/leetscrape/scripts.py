from .GenerateCodeStub import GenerateCodeStub
import argparse
from sqlalchemy import create_engine
from .utils import extract_solutions, upload_solutions

parser = argparse.ArgumentParser(
    description="Run this script to generate a code stub for the given question"
)
parser.add_argument(
    "--qid",
    metavar="Question ID",
    type=int,
    help="Enter a Leetcode question ID",
    required=False,
)
parser.add_argument(
    "--titleSlug",
    metavar="Title Slug",
    type=str,
    help="Enter a Leetcode question's title slug",
    required=False,
)
parser.add_argument(
    "-dB",
    "--database_string",
    metavar="sqlAlchemy database string",
    type=str,
    help="Enter sqlAlchemy database string",
    required=True,
)
parser.add_argument(
    "--solution_file",
    metavar="Solution File",
    type=str,
    help="Enter the path to the solution file",
    required=True,
)


def leetscrape_question():
    args = parser.parse_args()
    if not (args.qid or args.titleSlug):
        parser.error("At least one of qid or titleSlug need to be specified.")
    if args.qid:
        fcs = GenerateCodeStub(qid=args.qid)
    else:
        fcs = GenerateCodeStub(titleSlug=args.titleSlug)
    fcs.generate_code_stub_and_tests()


def leetupload_solution():
    args = parser.parse_args()
    if not args.qid or not args.solution_file:
        parser.error("QID and Solution file need to be passed.")
    engine = create_engine(args.database_string, echo=False)
    solutions = extract_solutions(args.solution_file)
    upload_solutions(engine, args.qid, solutions[args.qid])
